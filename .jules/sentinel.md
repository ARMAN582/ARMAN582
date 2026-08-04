# Sentinel's Journal

This journal records CRITICAL security learnings only, adhering to Sentinel's instructions.

## 2024-08-04 - DOM-based Cross-Site Scripting (XSS) Prevention
**Vulnerability:** Use of `.innerHTML` with dynamically concatenated values or static-appearing structures that could be vulnerable to DOM-based XSS when assets/data elements are modified.
**Learning:** Even in simple frontend HTML files with no backend, direct usage of `.innerHTML` to insert dynamic text elements is a risky habit and can lead to DOM XSS if any data is sourced from query parameters, external APIs, or user-controlled inputs.
**Prevention:** Always use safe DOM manipulation methods like `.textContent`, `.innerText`, and `document.createElement()` to safely handle text, or sanitize inputs prior to insertion.
