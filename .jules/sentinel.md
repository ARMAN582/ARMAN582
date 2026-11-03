# Sentinel Security Journal

This file records critical security learnings and vulnerability patterns discovered across the codebase.

## 2026-11-03 - Reverse Tabnabbing and Missing Content Security Policy
**Vulnerability:** External social links opened without `target="_blank"` and `rel="noopener noreferrer"`, exposing users to reverse tabnabbing attacks where the destination page can access and redirect `window.opener.location`. Additionally, lack of a Content Security Policy (CSP) allowed unrestricted script and resource loading origins.
**Learning:** In client-side HTML applications embedded directly within repository files like `README.md`, standard browser protections and restrictions must be declared via HTML `<meta>` tags and hardened attributes since no server-side security response headers exist.
**Prevention:** Always declare strict CSP rules via `<meta http-equiv="Content-Security-Policy">` and use `target="_blank" rel="noopener noreferrer"` for external anchors.
