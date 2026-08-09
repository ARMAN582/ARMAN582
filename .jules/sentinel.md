# Sentinel's Security Journal

## 2025-08-09 - Reverse Tabnabbing and Missing Content Security Policy in Embedded App
**Vulnerability:** External anchor links target `_blank` or similar without `rel="noopener noreferrer"`, exposing the app to reverse tabnabbing. Also, missing CSP header or `<meta>` tag allowed execution of unrestricted inline and external scripts/styles.
**Learning:** For a single-page HTML application embedded in a Markdown or HTML repo, client-side security mechanisms (like CSP meta tags and rel attributes) are crucial defense-in-depth measures.
**Prevention:** Always secure anchor links to external sites with `rel="noopener noreferrer"` and enforce a Content Security Policy via `<meta>` tag to limit loading to trusted sources.
