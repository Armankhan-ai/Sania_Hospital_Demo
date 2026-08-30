import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change title to Sania Hospital
    title_pattern = re.compile(r'<title>.*?</title>', re.IGNORECASE)
    content = title_pattern.sub('<title>Sania Hospital</title>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Updated title in {filename}')
