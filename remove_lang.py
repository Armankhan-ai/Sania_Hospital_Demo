from bs4 import BeautifulSoup
import os

files = ['Index.html', 'contact.html', 'appointment.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove ul with block-header__languages
        lang_uls = soup.find_all('ul', class_='block-header__languages')
        for ul in lang_uls:
            ul.decompose()
            
        # Remove div with block-header__overlay-languages
        overlay_langs = soup.find_all('div', class_='block-header__overlay-languages')
        for div in overlay_langs:
            div.decompose()
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Removed language switchers from {filename}")
