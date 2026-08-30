import os
from bs4 import BeautifulSoup

filename = 'about.html'
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # We want to keep the header and footer, but remove the homepage sections.
    # The homepage sections are: block-services, block-about, block-numbers, block-facilities, block-cta
    # Note: Our new hero is inside <main>. We must NOT remove it.
    
    classes_to_remove = ['block-services', 'block-about', 'block-numbers', 'block-facilities', 'block-cta']
    
    for cls in classes_to_remove:
        sections = soup.find_all('section', class_=cls)
        for section in sections:
            section.decompose()
            print(f"Removed section: {cls}")
            
    # Also, wait, let's see if there is an original block-hero outside of main.
    # In Index.html, block-hero is probably outside main!
    all_heroes = soup.find_all('section', class_='block-hero')
    for hero in all_heroes:
        # Check if it is inside main
        if not hero.find_parent('main', id='main'):
            hero.decompose()
            print("Removed original block-hero")
            
    # And same for block-why-us if there was an original one
    all_why_us = soup.find_all('section', class_='block-why-us')
    for why_us in all_why_us:
        if not why_us.find_parent('main', id='main'):
            why_us.decompose()
            print("Removed original block-why-us")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Cleaned up about.html")
