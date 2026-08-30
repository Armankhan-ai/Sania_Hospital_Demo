from bs4 import BeautifulSoup
import os

files = ['Index.html', 'contact.html', 'appointment.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove section with class block-logos
        logos_sections = soup.find_all(class_='block-logos')
        for section in logos_sections:
            section.decompose()
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Removed block-logos section from {filename}")
