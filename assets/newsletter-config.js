/* Offbeat AI Watch newsletter setting (run 9, decisions.md section 16 C5a). This file is the one place to switch on Kit.
   KIT_FORM_ID: the public ID of the owner's Kit form, the number in the form's embed code
   (for example https://app.kit.com/forms/1234567/subscriptions gives "1234567").
   While it is empty, the sign-up form on the home page stays exactly as it is. Once it is set, assets/kit-form.js swaps in
   Kit's embedded form for that ID (Kit keeps double opt-in, its default).
   KIT_FORM_UID (optional): the data-uid value from the same embed code. When it is set, Kit's own script (ck.5.js) also loads
   and shows Kit's inline messages; without it the form posts straight to Kit, which shows its own confirmation page.
   Both are public values printed in the page. Never put a Kit API key here. */
window.OFFBEAT_NEWSLETTER = { KIT_FORM_ID: "", KIT_FORM_UID: "" };
