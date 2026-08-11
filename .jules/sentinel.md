# Sentinel Security Journal

This is the security journal of Sentinel, protecting this repository against vulnerabilities and security risks.

## 2025-02-14 - [Reverse Tabnabbing and Missing Security Headers]
**Vulnerability:** The HTML page contained anchor links to external sites with `target="_blank"` missing or lacking proper `rel` attributes, and was missing standard browser security headers or client-side equivalences like CSP.
**Learning:** Single-page applications residing inside simple markdown or standalone files can still suffer from client-side attacks or tabnabbing if they link to external assets and/or do not constrain execution permissions.
**Prevention:** Always secure anchor links targeting external URLs with `target="_blank" rel="noopener noreferrer"`, and restrict execution via a client-side CSP meta tag.
