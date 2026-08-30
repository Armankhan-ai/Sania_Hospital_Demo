import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all occurrences of the old favicons with AA.avif
    new_content = re.sub(r'https://portfolio\.widehue\.co/rezonbio/wp-content/uploads/2025/09/favicon-150x150\.png', 'AA.avif', content)
    new_content = re.sub(r'https://portfolio\.widehue\.co/rezonbio/wp-content/uploads/2025/09/favicon-300x300\.png', 'AA.avif', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated favicons in {filename}')
    else:
        print(f'No old favicons found in {filename}')
