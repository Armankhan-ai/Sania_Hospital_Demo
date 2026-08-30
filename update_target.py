import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace target="_blank" or target=_blank with target="_self" (or remove it) 
    # ONLY for links where href="appointment.html"
    
    def replacement(match):
        # match.group(0) is the entire <a> tag up to >
        tag = match.group(0)
        # Replace target="_blank" or target=_blank inside this tag
        tag = re.sub(r'\s*target=[\'"]?_blank[\'"]?', '', tag, flags=re.IGNORECASE)
        # Also remove rel=noopener just in case, or leave it. 
        # But maybe safer to just replace target="_blank" with target="_self" to be explicit
        if 'target=' not in tag:
            # Let's insert target="_self" right after href
            tag = tag.replace('href="appointment.html"', 'href="appointment.html" target="_self"')
        return tag

    # Find <a> tags containing href="appointment.html"
    pattern = re.compile(r'<a\s+[^>]*?href=["\']appointment\.html["\'][^>]*?>', re.IGNORECASE)
    
    new_content, count = pattern.subn(replacement, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {count} links in {filename}')
    else:
        print(f'No links to update in {filename}')
