import os
import glob

# Files to process
html_files = glob.glob("*.html")

# The replacement for the main header logo block
old_header_logo = """<img alt="Logo" src="AA.png" style="max-height: 40px; width: auto;"/>
<div style="display: flex; flex-direction: column; line-height: 1.2;">
<span style="font-weight: bold; font-size: 1.2rem; color: var(--wp--preset--color--black, #000);">Sania Hospital</span>
<span style="font-size: 0.75rem; color: var(--wp--preset--color--gray, #666);">Advanced Care. Compassionate Healing.</span>
</div>"""

new_header_logo = """<div style="display: flex; flex-direction: column; justify-content: center;">
<span style="font-weight: 900; font-size: 1.8rem; letter-spacing: 1px; color: #1e3a8a; text-transform: uppercase; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); line-height: 1; font-family: 'Arial', sans-serif;">SANIA HOSPITAL</span>
<span style="font-size: 0.75rem; font-weight: 600; color: #0ea5e9; text-transform: uppercase; letter-spacing: 2px; margin-top: 4px;">Advanced Care. Compassionate Healing.</span>
</div>"""

# The replacement for loader logo (mostly in index.html)
old_loader_logo = '<img class="block-hero__loader-logo" src="AA.png" style="width: 150px; height: auto; object-fit: contain; position: relative; z-index: 10;"/>'
new_loader_logo = '<div class="block-hero__loader-logo" style="position: relative; z-index: 10; text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%; height: 100%;"><span style="font-weight: 900; font-size: 3rem; letter-spacing: 2px; color: #ffffff; text-transform: uppercase; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); font-family: \'Arial\', sans-serif; line-height: 1.1;">SANIA<br>HOSPITAL</span></div>'

# The replacement for footer logo
old_footer_logo = '<img alt="Sania Hospital" src="AA.png" style="height: 32px; width: auto;"/>'
new_footer_logo = '<span style="font-weight: 900; font-size: 1.5rem; letter-spacing: 1px; color: #ffffff; text-transform: uppercase; font-family: \'Arial\', sans-serif;">SANIA HOSPITAL</span>'

for file_path in html_files:
    if file_path == 'original.html' or file_path == 'scratch_snippet.html':
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply replacements
    content = content.replace(old_header_logo, new_header_logo)
    content = content.replace(old_loader_logo, new_loader_logo)
    content = content.replace(old_footer_logo, new_footer_logo)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Logo replaced successfully in all HTML files.")
