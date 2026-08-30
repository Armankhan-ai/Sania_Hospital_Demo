import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon already exists
    if 'rel="icon"' in content:
        print(f'{filename} already has an icon.')
        continue
    
    # Add favicon right after the </title> tag
    pattern = re.compile(r'(<title>.*?</title>)', re.IGNORECASE)
    
    def replacement(match):
        return match.group(1) + '\n    <link rel="icon" href="AA.avif" type="image/avif">'

    new_content, count = pattern.subn(replacement, content, count=1)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Added favicon to {filename}')
    else:
        print(f'No title tag found in {filename}')
