import os
import glob
import re

files_to_update = ['about.html', 'contact.html', 'appointment.html']

new_header_content = """<div style="display: flex; align-items: center; gap: 12px;">
    <div style="display: flex; flex-direction: column; justify-content: center;">
        <span style="font-weight: 900; font-size: 1.6rem; letter-spacing: 0.5px; color: #0f172a; text-transform: uppercase; line-height: 1; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">SANIA <span style="color: #0284c7;">HOSPITAL</span></span>
        <span style="font-size: 0.7rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-top: 3px;">Advanced Care. Compassionate Healing.</span>
    </div>
</div>"""

# Regex to match the insides of <a class="block-header__logo" ...> ... </a>
header_logo_regex = re.compile(r'(<a[^>]*class="block-header__logo"[^>]*>)\s*<img[^>]*>\s*<div[^>]*>.*?</div>\s*(</a>)', re.DOTALL)

# For footer, replacing <img alt="Sania Hospital" src="AA.png" .../>
footer_img_regex = re.compile(r'<img alt="Sania Hospital" src="AA.png"[^>]*/>')

new_footer_content = """<div style="display: flex; align-items: center; gap: 10px;">
    <span style="font-weight: 900; font-size: 1.4rem; letter-spacing: 1px; color: #ffffff; text-transform: uppercase; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">SANIA <span style="color: #38bdf8;">HOSPITAL</span></span>
</div>"""

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update header
    content = header_logo_regex.sub(r'\1\n' + new_header_content + r'\n\2', content)

    # Update footer
    content = footer_img_regex.sub(new_footer_content, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated missing files.")
