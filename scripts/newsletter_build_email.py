#!/usr/bin/env python3
"""Build the newsletter email for one Offbeat AI Watch issue.

Reads an issue page (issues/YYYY-MM-DD.html) and writes:
  <out>/email.json  subject, preview text, HTML content, issue address, marker
  <out>/email.html  the email body, to look at in a browser
  <out>/summary.txt a plain text summary for the workflow log

It never makes a network call and never reads any secret. Only the Python
standard library is used.

  subject      = the issue's H1
  preview text = the issue's <meta name="description">
  body         = the issue's opening paragraph, the headlines of the other
                 stories, and a "Read the full issue" link to
                 https://gtmhelix.com/ai-trendwatch/issues/<file>

Usage:
  python scripts/newsletter_build_email.py --issue issues/2026-01-07.html --out build/newsletter
  python scripts/newsletter_build_email.py --latest --out build/newsletter --dry-run
"""

import argparse
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

SITE_BASE = "https://gtmhelix.com/ai-trendwatch/"
ISSUE_RE = re.compile(r"^issues/\d{4}-\d{2}-\d{2}\.html$")
MAX_HEADLINES = 6


class IssueParser(HTMLParser):
    """Collects the H1, the meta description, the first lead paragraph and story headlines."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.h1 = ""
        self.description = ""
        self.lead = ""
        self.headlines = []
        self._stack = []  # (tag, kind) for elements we are collecting text from
        self._buf = []
        self._h1_done = False
        self._lead_done = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "meta" and (a.get("name") or "").lower() == "description" and not self.description:
            self.description = (a.get("content") or "").strip()
            return
        kind = None
        if tag == "h1" and not self._h1_done:
            kind = "h1"
        elif tag == "p" and "story-text" in classes and not self._lead_done:
            kind = "lead"
        elif tag in ("h2", "h3", "h4") and "story-headline" in classes:
            kind = "headline"
        if kind and not self._stack:
            self._stack.append((tag, kind))
            self._buf = []
        elif self._stack and tag == self._stack[0][0]:
            # nested element with the same tag name: track depth
            self._stack.append((tag, None))

    def handle_endtag(self, tag):
        if not self._stack or tag != self._stack[-1][0]:
            return
        _, kind = self._stack.pop()
        if self._stack:
            return
        text = " ".join("".join(self._buf).split())
        if kind == "h1":
            self.h1, self._h1_done = text, True
        elif kind == "lead":
            self.lead, self._lead_done = text, True
        elif kind == "headline" and text:
            self.headlines.append(text)

    def handle_data(self, data):
        if self._stack:
            self._buf.append(data)


def latest_issue(repo_root):
    folder = os.path.join(repo_root, "issues")
    names = sorted(n for n in os.listdir(folder) if ISSUE_RE.match("issues/" + n))
    if not names:
        raise SystemExit("No issue files found under issues/")
    return "issues/" + names[-1]


def build(issue_path, repo_root="."):
    rel = issue_path.replace("\\", "/")
    if rel.startswith("./"):
        rel = rel[2:]
    if not ISSUE_RE.match(rel):
        raise SystemExit(f"'{rel}' is not an issue file (expected issues/YYYY-MM-DD.html)")
    full = os.path.join(repo_root, rel)
    with open(full, encoding="utf-8") as f:
        parser = IssueParser()
        parser.feed(f.read())

    subject = parser.h1
    preview = parser.description
    if not subject:
        raise SystemExit(f"{rel} has no H1, so there is no subject line")
    if not preview:
        raise SystemExit(f"{rel} has no meta description, so there is no preview text")

    url = SITE_BASE + rel
    def e(text):
        return html.escape(text, quote=False)

    parts = [f"<h1>{e(subject)}</h1>"]
    if parser.lead:
        parts.append(f"<p>{e(parser.lead)}</p>")
    headlines = parser.headlines[:MAX_HEADLINES]
    if headlines:
        parts.append("<p><strong>Also in this issue:</strong></p>")
        parts.append("<ul>" + "".join(f"<li>{e(h)}</li>" for h in headlines) + "</ul>")
    parts.append(f'<p><a href="{html.escape(url)}">Read the full issue</a></p>')
    parts.append("<p>You are receiving this because you subscribed to Offbeat AI Watch at gtmhelix.com.</p>")
    content = "\n".join(parts)

    return {
        "issue_path": rel,
        "issue_url": url,
        "subject": subject,
        "preview_text": preview,
        "lead": parser.lead,
        "headlines": headlines,
        "content": content,
        # Kit's internal description. The send step uses it to refuse a second
        # broadcast for the same issue.
        "marker": "offbeat:" + rel,
    }


def main():
    ap = argparse.ArgumentParser(description="Build the newsletter email for one issue (no network).")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--issue", help="issue file, for example issues/2026-01-07.html")
    g.add_argument("--latest", action="store_true", help="use the newest file under issues/")
    ap.add_argument("--out", default="build/newsletter", help="output folder")
    ap.add_argument("--repo", default=".", help="repository root")
    ap.add_argument("--dry-run", action="store_true",
                    help="label the output as a dry run (this script never uses the network either way)")
    args = ap.parse_args()

    issue = latest_issue(args.repo) if args.latest else args.issue
    email = build(issue, args.repo)
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "email.json"), "w", encoding="utf-8") as f:
        json.dump(email, f, ensure_ascii=False, indent=2)
    with open(os.path.join(args.out, "email.html"), "w", encoding="utf-8") as f:
        f.write("<!doctype html><meta charset=\"utf-8\"><title>" + html.escape(email["subject"]) +
                "</title>\n" + email["content"] + "\n")

    lines = [
        ("DRY RUN: " if args.dry_run else "") + "Newsletter email built. No network call was made.",
        f"Issue file:   {email['issue_path']}",
        f"Issue link:   {email['issue_url']}",
        f"Subject:      {email['subject']}",
        f"Preview text: {email['preview_text']}",
        f"Preview text length: {len(email['preview_text'])} characters",
        f"Opening paragraph: {email['lead'] or '(none found)'}",
        "Other headlines:" if email["headlines"] else "Other headlines: (none found)",
    ]
    lines += [f"  - {h}" for h in email["headlines"]]
    lines += ["HTML body:", email["content"]]
    text = "\n".join(lines) + "\n"
    with open(os.path.join(args.out, "summary.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
