# Sentinel Security Journal

## 2025-05-18 - Standalone HTML Single-Page Application Hardening
**Vulnerability:** External third-party links opened without `rel="noopener noreferrer"` and missing Content Security Policy (CSP) headers in a single-page HTML application.
**Learning:** Standalone HTML apps hosted directly via files or file viewers lack server-configured HTTP response headers (such as CSP, X-Frame-Options, or Referrer-Policy). When opened in browsers, external navigation without `noopener` / `noreferrer` allows reverse tabnabbing via `window.opener.location`, and lack of a CSP `<meta>` tag leaves the page open to unauthorized network calls or injected script sources if content is extended.
**Prevention:** Always declare `<meta http-equiv="Content-Security-Policy" ...>` in head to enforce strict source boundaries (`default-src 'none'`), and ensure all outbound anchor tags use `target="_blank" rel="noopener noreferrer"`.
