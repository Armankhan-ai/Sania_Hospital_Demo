import os
import glob
import re

html_files = glob.glob("*.html")

# Regex to match the div containing the plus icon SVG, optionally followed by newlines and spaces.
# We'll remove this entirely.
plus_icon_regex = re.compile(r'\s*<div style="background-color: #e11d48;[^>]*>\s*<svg[^>]*><path d="M12 2v20M2 12h20"/></svg>\s*</div>', re.DOTALL)

for file_path in html_files:
    if file_path == 'original.html' or file_path == 'scratch_snippet.html':
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply replacement (remove the match)
    content = plus_icon_regex.sub('', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Removed + marks successfully.")
