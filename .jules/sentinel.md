# Sentinel Security Journal

This is the security journal of Sentinel, protecting this repository against vulnerabilities and security risks.

## 2026-11-02 - Reverse Tabnabbing and Missing Content Security Policy
**Vulnerability:** External social links opened without `target="_blank"` and `rel="noopener noreferrer"`, exposing users to reverse tabnabbing attacks where the target tab can alter `window.opener.location`. Furthermore, missing CSP allowed unrestricted loading of arbitrary origins.
**Learning:** Even static/embedded HTML applications in `README.md` require defensive link attributes and CSP restrictions to prevent cross-origin tampering and unauthorized script/asset inclusion.
**Prevention:** Always specify `target="_blank" rel="noopener noreferrer"` for external hyperlinks and configure a strict `Content-Security-Policy` meta tag.
