import os
import re

def remove_empty_spaces():
    with open('about.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The user states there's a big empty section between block-why-us and CTA.
    # In earlier versions, there was a lot of padding or a spacer.
    # Let's just remove any <br> tags, empty <section> or <div> tags between these parts, or clean up newlines.
    
    # We will use BeautifulSoup to remove completely empty sections or spacers.
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    why_us = soup.find('section', class_='block-why-us')
    cta = soup.find(lambda tag: tag.name == 'section' and 'Ready to Book an Appointment?' in tag.text and 'block-why-us' not in tag.get('class', []))
    
    if why_us and cta:
        # iterate nodes between why_us and cta
        current = why_us.next_sibling
        nodes_to_remove = []
        while current and current != cta:
            # If it's an element, check if it's empty
            if current.name:
                text = current.get_text(strip=True)
                # If there's no text and no images/iframes
                if not text and not current.find(['img', 'iframe', 'video']):
                    nodes_to_remove.append(current)
            current = current.next_sibling
            
        for node in nodes_to_remove:
            node.decompose()

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Done removing empty spaces")

if __name__ == '__main__':
    remove_empty_spaces()
