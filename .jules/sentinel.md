# Sentinel's Security Journal

This journal tracks critical security learnings, vulnerability patterns, and architectural constraints specific to this codebase.

## 2025-08-08 - Secure HTML & JS Sanitization in Embedded Apps
**Vulnerability:** Embedded interactive HTML pages lack default Content Security Policy (CSP), open external links without `noopener noreferrer` (making them vulnerable to tabnabbing), and may dynamically render un-escaped variables using `innerHTML` leading to potential Cross-Site Scripting (XSS) or HTML Injection.
**Learning:** Static/embedded single-file web applications often overlook client-side sanitization. When rendering data dynamically using string concatenation (e.g., using `assets` list), developers can easily introduce XSS or code execution entry points if external inputs or un-escaped properties are used. Furthermore, missing strict CSP rules allows inline script executions without protection or cross-origin data exfiltration if the application gets extended.
**Prevention:**
- Always enforce a strict `Content-Security-Policy` meta header to limit code sources.
- Never write untrusted/dynamic variables to `.innerHTML` without escaping them first using a robust `escapeHTML` function or using safe alternatives like `.textContent`/`.innerText`.
- Ensure all outbound anchors use `target="_blank"` with `rel="noopener noreferrer"` to prevent malicious parent redirection (reverse tabnabbing).
