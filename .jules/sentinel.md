# Sentinel Security Journal

## 2025-08-13 - [Reverse Tabnabbing and Lack of CSP in Single-Page HTML App]
**Vulnerability:** The application features social media links that lack `target="_blank" rel="noopener noreferrer"` attributes, leaving them vulnerable to reverse tabnabbing where a malicious linked page could control the parent window. Additionally, there was no Content Security Policy (CSP) header or meta tag, allowing unauthorized scripts/styles or frame/asset injection.
**Learning:** Legacy or standalone HTML templates embedded in `README.md` or static hosts often omit basic security headers and attributes because they are treated as simple documents rather than secure applications.
**Prevention:** Ensure all external links include `target="_blank" rel="noopener noreferrer"`. Always embed a restrictive Content Security Policy (`<meta http-equiv="Content-Security-Policy" content="...">`) in the document head to limit resource execution to safe origins.
