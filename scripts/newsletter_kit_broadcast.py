#!/usr/bin/env python3
"""Create and schedule the Kit broadcast for one built newsletter email.

Input: the email.json written by scripts/newsletter_build_email.py.

Settings come from environment variables:
  KIT_API_KEY         the Kit V4 API key, a secret of the newsletter-send
                      environment (so only job 2 has it). Used only as the
                      X-Kit-Api-Key request header. Never printed, and not
                      read in a dry run.
  KIT_SEGMENT_ID      optional. Send only to this Kit segment. Empty means
                      Kit's default, all subscribers.
  KIT_PUBLIC          optional, "true" (default) or "false". Kit's update
                      reference says scheduling needs public set to true.
  SEND_DELAY_MINUTES  optional, default 30, at least 10. The broadcast is
                      scheduled this many minutes after approval, so there is
                      time to cancel it in Kit.
  WAIT_LIVE_MINUTES   optional, default 20. How long to wait for the issue
                      page to be live before giving up (nothing is created).

Behaviour:
  - KIT_API_KEY missing: prints one line and exits 0 (clean skip).
  - --dry-run: prints the request it would send and makes no network call at
    all. It does not read the key.
  - Otherwise: waits until the issue page is live, refuses to create a second
    broadcast for the same issue, then POSTs https://api.kit.com/v4/broadcasts
    with a send_at time.

Only the Python standard library is used.
"""

import argparse
import html
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.kit.com/v4"
IST = timezone(timedelta(hours=5, minutes=30))


def log(line):
    print(line, flush=True)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(line + "\n\n")


def fail(line):
    log("FAILED: " + line)
    sys.exit(1)


def int_setting(name, default, minimum):
    raw = (os.environ.get(name) or "").strip()
    if not raw:
        return default
    if not raw.isdigit():
        fail(f"{name} must be a whole number of minutes")
    value = int(raw)
    if value < minimum:
        fail(f"{name} must be at least {minimum}")
    return value


def build_body(email, now):
    seg = (os.environ.get("KIT_SEGMENT_ID") or "").strip()
    if seg and not seg.isdigit():
        fail("KIT_SEGMENT_ID must be a number (or empty for all subscribers)")
    public = (os.environ.get("KIT_PUBLIC") or "true").strip().lower() != "false"
    delay = int_setting("SEND_DELAY_MINUTES", 30, 10)
    send_at = now + timedelta(minutes=delay)
    body = {
        "subject": email["subject"],
        "preview_text": email["preview_text"],
        "content": email["content"],
        "description": email["marker"],
        "public": public,
        "published_at": now.isoformat(timespec="seconds"),
        "send_at": send_at.isoformat(timespec="seconds"),
    }
    if seg:
        body["subscriber_filter"] = [{"all": [{"type": "segment", "ids": [int(seg)]}], "any": None, "none": None}]
    return body, send_at


class Kit:
    def __init__(self, key):
        self._key = key

    def call(self, method, path, body=None):
        data = None if body is None else json.dumps(body).encode("utf-8")
        req = urllib.request.Request(API + path, data=data, method=method, headers={
            "X-Kit-Api-Key": self._key,
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "offbeat-newsletter-workflow",
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            detail = e.read()[:300].decode("utf-8", "replace").replace(self._key, "[hidden]")
            fail(f"Kit {method} {path} returned HTTP {e.code}: {detail}")
        except urllib.error.URLError as e:
            fail(f"Kit {method} {path} could not be reached: {e.reason}")

    def existing_for(self, marker):
        """Return the id of a broadcast already made for this issue, or None."""
        after = None
        for _ in range(20):
            path = "/broadcasts?per_page=500" + (f"&after={urllib.parse.quote(str(after))}" if after else "")
            res = self.call("GET", path)
            for b in res.get("broadcasts", []):
                if (b.get("description") or "") == marker:
                    return b.get("id")
            info = res.get("pagination") or {}
            if not info.get("has_next_page"):
                return None
            after = info.get("end_cursor")
        return None


def wait_until_live(url, subject, minutes):
    deadline = time.time() + minutes * 60
    while True:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "offbeat-newsletter-workflow"})
            with urllib.request.urlopen(req, timeout=20) as r:
                page = html.unescape(r.read().decode("utf-8", "replace"))
            if subject in page:
                log(f"The issue is live: {url}")
                return
        except (urllib.error.URLError, TimeoutError):
            pass
        if time.time() > deadline:
            fail(f"{url} was not live with the issue headline after {minutes} minutes, so no broadcast was created")
        time.sleep(30)


def main():
    ap = argparse.ArgumentParser(description="Create and schedule the Kit broadcast for one issue.")
    ap.add_argument("--email", default="build/newsletter/email.json", help="email.json from the build step")
    ap.add_argument("--dry-run", action="store_true", help="print the request and make no network call")
    args = ap.parse_args()

    with open(args.email, encoding="utf-8") as f:
        email = json.load(f)

    now = datetime.now(timezone.utc)
    body, send_at = build_body(email, now)
    when = send_at.astimezone(IST).strftime("%d %b %Y %H:%M IST")

    if args.dry_run:
        log("DRY RUN: no network call was made. This is the request that would be sent after approval:")
        log(f"POST {API}/broadcasts")
        # A dry run runs in job 1, outside the newsletter-send environment, so it never has the key and never reads it.
        log("Header X-Kit-Api-Key: [not read in a dry run. Job 2 reads it from the KIT_API_KEY secret of the "
            "newsletter-send environment and never prints it]")
        log(json.dumps(body, ensure_ascii=False, indent=2))
        log(f"It would be scheduled for {when}, after first checking that {email['issue_url']} is live "
            f"and that no broadcast with the description '{email['marker']}' exists.")
        return

    key = os.environ.get("KIT_API_KEY") or ""
    if not key:
        log("SKIPPED: the KIT_API_KEY secret of the newsletter-send environment is not set, so no Kit broadcast was created.")
        return

    wait_until_live(email["issue_url"], email["subject"], int_setting("WAIT_LIVE_MINUTES", 20, 1))
    kit = Kit(key)
    existing = kit.existing_for(email["marker"])
    if existing:
        log(f"Kit broadcast {existing} already exists for {email['issue_path']}. Nothing new was created.")
        return

    res = kit.call("POST", "/broadcasts", body)
    b = res.get("broadcast", {})
    log(f"Scheduled Kit broadcast {b.get('id')} for {when}: {email['subject']}")
    log(f"To stop it before then: in Kit open Send, then Broadcasts, find it under Scheduled, and delete it or turn it back into a draft.")


if __name__ == "__main__":
    main()
