KISAN ELECTRICALS — DEPLOYMENT NOTES

This website is intentionally built with plain HTML, CSS and vanilla JavaScript.
It does not require PHP, Laravel, Node.js or a database to run.

VERCEL
1. Create a new Vercel project.
2. Upload/import this folder as the project root.
3. Select "Other" if Vercel asks for a framework.
4. Leave the build command empty and deploy.

CONVENTIONAL HOSTING
Upload the contents of this folder into public_html (or the domain's document root).

BEFORE USING A NEW DOMAIN
The current generated canonical URLs use https://kisan-electricals.vercel.app.
If the final domain is different, update BASE_URL in scripts/build_site.py and run:

  python3 scripts/build_site.py

The public pages themselves remain fully static after generation.

BUSINESS INFORMATION
Review the phone number, address, working hours, map link and product availability
before launch. Prices and changing stock are deliberately not hard-coded.
