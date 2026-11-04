# Sentinel Security Journal

## 2026-04-06 - Client-Side Content Security Policy for Embedded HTML Applications
**Vulnerability:** Without server-side infrastructure, applications hosted directly from markdown/HTML files (such as GitHub profile or documentation viewers) lack HTTP response headers, leaving them vulnerable to injection of untrusted third-party scripts or unauthorized network exfiltration if inputs or DOM elements are manipulated.
**Learning:** Because this application is entirely contained within `README.md` and served statically or opened as a local/preview HTML document, server-set security headers like CSP or X-Frame-Options cannot be delivered via HTTP headers. A `<meta http-equiv="Content-Security-Policy">` tag provides defense-in-depth by restricting sources for scripts, styles, objects, and base URIs directly at the browser rendering layer.
**Prevention:** For self-contained HTML applications lacking backend servers, always declare a strict `<meta http-equiv="Content-Security-Policy">` in the document `<head>` restricting script, style, and object execution to trusted sources.
