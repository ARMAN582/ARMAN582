# Sentinel's Security Journal

## 2026-08-07 - DOM XSS & Reverse Tabnabbing Mitigation in Single-Page Market Simulation App
**Vulnerability:** DOM-based Cross-Site Scripting (XSS) via dynamic template literals assigned to `innerHTML` when rendering asset cards, and reverse tabnabbing via social media links lacking standard target isolation attributes (`target="_blank"` without `rel="noopener noreferrer"`).
**Learning:** Single-page applications directly embedded in `README.md` or as simple HTML pages are highly susceptible to DOM-based security patterns due to standard template rendering convenience over strict browser isolation context. Injections in asset lists or custom assets added dynamically could evaluate malicious scripts inside the document context.
**Prevention:** Always prioritize structured DOM API methods (`createElement`, `textContent`, `appendChild`) over raw string string manipulation and `innerHTML`. Consistently apply `rel="noopener noreferrer"` to external links targeting separate browser execution threads to prevent parent document reference hijacking.
