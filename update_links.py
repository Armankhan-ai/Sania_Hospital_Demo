import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replacement(match):
        return f'{match.group(1)}href={match.group(2)}appointment.html{match.group(2)}{match.group(4)}'

    pattern = re.compile(r'(<a\s+[^>]*?)href=([\'"])(?:tel:\+919414890852|https://rezonbio\.dayschedule\.com/?)([\'"])([^>]*?>\s*(?:Book Appointment|Book a meeting|Meet Our Business Team)\s*</a>)', re.IGNORECASE)
    
    new_content, count = pattern.subn(replacement, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f'Updated {filename}: {count} matches replaced')
