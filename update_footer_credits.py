from bs4 import BeautifulSoup
import os

files = ['Index.html', 'contact.html', 'appointment.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find the footer credits link
        credits_link = soup.find('a', class_='block-footer__credits')
        if credits_link:
            credits_link['href'] = 'https://intvarautomation.online'
            credits_link['title'] = 'Design by INTVAR'
            credits_link.string = 'Design by INTVAR'
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Updated footer credits in {filename}")
