import os
import glob
import re

html_files = glob.glob("*.html")

# The regex to match the previous logo we added
header_regex = re.compile(r'<div style="display: flex; flex-direction: column; justify-content: center;">\s*<span style="font-weight: 900; font-size: 1.8rem; letter-spacing: 1px; color: #1e3a8a; text-transform: uppercase; text-shadow: 1px 1px 2px rgba\(0,0,0,0\.2\); line-height: 1; font-family: \'Arial\', sans-serif;">SANIA HOSPITAL</span>\s*<span style="font-size: 0.75rem; font-weight: 600; color: #0ea5e9; text-transform: uppercase; letter-spacing: 2px; margin-top: 4px;">Advanced Care\. Compassionate Healing\.</span>\s*</div>', re.DOTALL)

new_header_logo = """<div style="display: flex; align-items: center; gap: 12px;">
    <div style="background-color: #e11d48; width: 36px; height: 36px; border-radius: 8px; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 6px rgba(225,29,72,0.3);">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/></svg>
    </div>
    <div style="display: flex; flex-direction: column; justify-content: center;">
        <span style="font-weight: 900; font-size: 1.6rem; letter-spacing: 0.5px; color: #0f172a; text-transform: uppercase; line-height: 1; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">SANIA <span style="color: #0284c7;">HOSPITAL</span></span>
        <span style="font-size: 0.7rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-top: 3px;">Advanced Care. Compassionate Healing.</span>
    </div>
</div>"""

# For the loader
loader_regex = re.compile(r'<div class="block-hero__loader-logo".*?>\s*<span.*?>SANIA<br>HOSPITAL</span>\s*</div>', re.DOTALL)
new_loader_logo = """<div class="block-hero__loader-logo" style="position: relative; z-index: 10; display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%; height: 100%; gap: 15px;">
    <div style="background-color: #e11d48; width: 60px; height: 60px; border-radius: 12px; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 10px rgba(225,29,72,0.5);">
        <svg xmlns="http://www.w3.org/2000/svg" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/></svg>
    </div>
    <span style="font-weight: 900; font-size: 2.5rem; letter-spacing: 2px; color: #ffffff; text-transform: uppercase; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.1; text-align: center;">SANIA<br><span style="color: #38bdf8;">HOSPITAL</span></span>
</div>"""

# For the footer
footer_regex = re.compile(r'<span style="font-weight: 900; font-size: 1\.5rem; letter-spacing: 1px; color: #ffffff; text-transform: uppercase; font-family: \'Arial\', sans-serif;">SANIA HOSPITAL</span>', re.DOTALL)
new_footer_logo = """<div style="display: flex; align-items: center; gap: 10px;">
    <div style="background-color: #e11d48; width: 28px; height: 28px; border-radius: 6px; display: flex; justify-content: center; align-items: center;">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/></svg>
    </div>
    <span style="font-weight: 900; font-size: 1.4rem; letter-spacing: 1px; color: #ffffff; text-transform: uppercase; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">SANIA <span style="color: #38bdf8;">HOSPITAL</span></span>
</div>"""

for file_path in html_files:
    if file_path == 'original.html' or file_path == 'scratch_snippet.html':
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply replacements
    content = header_regex.sub(new_header_logo, content)
    content = loader_regex.sub(new_loader_logo, content)
    content = footer_regex.sub(new_footer_logo, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Logo updated with hospital theme successfully.")
