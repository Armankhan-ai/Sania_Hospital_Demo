import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace specific external links to #
    links_to_remove = [
        r'https://portfolio\.widehue\.co/rezonbio/careers/',
        r'https://portfolio\.widehue\.co/rezonbio/discover/company-leadership/',
        r'https://portfolio\.widehue\.co/rezonbio/newsroom/',
        r'https://portfolio\.widehue\.co/rezonbio/pl/',
        r'https://portfolio\.widehue\.co/rezonbio/solutions/gmp-manufacturing/',
        r'https://poir\.opi\.org\.pl/en/',
        r'https://intvarautomation\.online',
        r'https://www\.linkedin\.com/company/rezonbio/',
        r'https://portfolio\.widehue\.co/rezonbio/\?p=337',
        r'https://portfolio\.widehue\.co/rezonbio/'
    ]
    
    for link in links_to_remove:
        # We replace href="link" with href="#"
        content = re.sub(rf'href=[\'"]{link}["\']', 'href="#"', content)
        
    # Fix the contact link which should point to contact.html
    content = re.sub(r'href=[\'"]https://portfolio\.widehue\.co/rezonbio/contact/["\']', 'href="contact.html"', content)

    # 2. Replace text mentions of Rezon Bio
    # Be careful not to break HTML tags or URLs. We'll do a simple string replace for the exact casing.
    content = content.replace('Rezon Bio', 'Sania Hospital')
    content = content.replace('Rezon bio', 'Sania Hospital')
    content = content.replace('RezonBio', 'Sania Hospital')
    content = content.replace('rezon bio', 'sania hospital')
    
    # Also there might be things like "Where Dedication Delivers Excellence" -> maybe leave it or change it.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Cleaned up Rezon Bio data in {filename}')
