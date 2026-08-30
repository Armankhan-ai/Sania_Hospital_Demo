import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to remove the block-separator section
    # We want to match <section class="block-separator container-full" ... </section>
    pattern = re.compile(r'<section class="block-separator container-full".*?</section>', re.IGNORECASE | re.DOTALL)
    
    new_content, count = pattern.subn('', content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Removed {count} block-separator section(s) from {filename}')
    else:
        print(f'No block-separator section found in {filename}')
