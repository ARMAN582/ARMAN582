# Sentinel Security Journal

## 2024-08-14 - Securing Standalone HTML Embedded in README.md
**Vulnerability:** Reverse tabnabbing (tabjacking) via target="_blank" links and lack of resource defense-in-depth (lack of Content Security Policy).
**Learning:** Standalone frontend web applications embedded inside repository `README.md` files are vulnerable to clickjacking, unauthorized resource loading, or tabjacking if their outbound social links and layout are not secured, as there are no backend-driven HTTP headers to protect them.
**Prevention:** Always include `rel="noopener noreferrer"` on all outbound anchors opening in new tabs, and embed a strict Content Security Policy (CSP) meta tag directly into the document's `<head>` to lock down resource loading to local origin only.
