import os
from bs4 import BeautifulSoup

filename = 'about.html'
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all forms
    forms = soup.find_all('form')
    for form in forms:
        # Find the parent block-contactform or section
        parent_section = form.find_parent('section', class_='block-contactform')
        if parent_section:
            parent_section.decompose()
            print("Removed section.block-contactform")
        else:
            parent_div = form.find_parent('div', class_='wp-site-blocks')
            if parent_div:
                 print("Found form inside wp-site-blocks but not in block-contactform")
                 # just decompose the form container
                 container = form.find_parent('div', class_='wpcf7')
                 if container:
                     container.decompose()
            else:
                 form.decompose()
                 
    # We should also check for any sections with id 'contact' or class 'block-contactform' just in case
    contact_sections = soup.find_all('section', class_='block-contactform')
    for section in contact_sections:
        section.decompose()
        print("Removed a block-contactform section")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Updated {filename}")
