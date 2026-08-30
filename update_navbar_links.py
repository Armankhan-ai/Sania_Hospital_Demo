import os
from bs4 import BeautifulSoup

files = ['Index.html', 'contact.html', 'appointment.html', 'about.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all anchor tags in the nav
        nav = soup.find('nav', class_='block-header__nav')
        if nav:
            links = nav.find_all('a')
            for link in links:
                href = link.get('href', '')
                # Fix Departments link
                if href == '#specialities' or href == 'Index.html#specialities':
                    link['href'] = 'Index.html#specialities'
                # Fix Gallery link
                if href == '#gallery' or href == 'Index.html#gallery':
                    link['href'] = 'Index.html#gallery'
                    
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Updated navbar in {filename}")
