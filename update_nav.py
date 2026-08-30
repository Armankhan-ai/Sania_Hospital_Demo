import os
from bs4 import BeautifulSoup

files = ['Index.html', 'contact.html', 'appointment.html', 'about.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all anchor tags that have href="#about"
        nav_links = soup.find_all('a', href='#about')
        for link in nav_links:
            link['href'] = 'about.html'
            link.string = 'About Us'
            
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Updated nav in {filename}")
