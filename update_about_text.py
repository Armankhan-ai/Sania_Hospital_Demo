import os
from bs4 import BeautifulSoup

filename = 'about.html'
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # Update the hero description
    hero_desc = soup.find('p', class_='block-hero__description')
    if hero_desc:
        hero_desc.string = "Driven by care. Powered by trust. A multi & super speciality hospital with a relentless passion for patient safety."
        
    # Update the History section to include the new text
    history_heading = soup.find(lambda tag: tag.name == 'h2' and 'Our History' in tag.text)
    if history_heading:
        history_p = history_heading.find_next_sibling('p')
        if history_p:
            # Append the new sentence or replace it
            history_p.string = "We are delivering advanced multispecialty healthcare to increase access to much-needed critical care for the people of Alwar. Established in 2004, Sania Hospital was founded with a vision to provide the best and most comprehensive medical care to the region."

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Updated about.html text")
