/* Offbeat AI Watch (run 9 C5a): swap in Kit's embedded form when assets/newsletter-config.js sets KIT_FORM_ID.
   While KIT_FORM_ID is empty (or not a number) this script does nothing, so the current form stays exactly as it is. */
(function () {
  var cfg = window.OFFBEAT_NEWSLETTER || {};
  var id = String(cfg.KIT_FORM_ID || "").trim();
  var uid = String(cfg.KIT_FORM_UID || "").trim();
  if (!/^\d+$/.test(id)) return;
  var old = document.querySelector("form.subscribe-form");
  if (!old) return;
  var f = document.createElement("form");
  f.action = "https://app.kit.com/forms/" + id + "/subscriptions";
  f.method = "post";
  f.className = "subscribe-form seva-form formkit-form";
  f.setAttribute("data-sv-form", id);
  f.setAttribute("data-format", "inline");
  f.setAttribute("data-version", "5");
  if (/^[0-9a-f]+$/i.test(uid)) f.setAttribute("data-uid", uid);
  f.innerHTML = '<ul class="formkit-alert formkit-alert-error" data-element="errors" data-group="alert"></ul>' +
    '<input class="formkit-input" type="email" name="email_address" aria-label="Email address" placeholder="Enter your email" required>' +
    '<button type="submit" class="formkit-submit" data-element="submit"><span>Subscribe</span></button>';
  old.parentNode.replaceChild(f, old);
  if (f.getAttribute("data-uid")) {
    var s = document.createElement("script");
    s.src = "https://f.convertkit.com/ckjs/ck.5.js";
    s.async = true;
    document.body.appendChild(s);
  }
})();
