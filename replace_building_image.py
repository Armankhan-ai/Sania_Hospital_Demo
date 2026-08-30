from bs4 import BeautifulSoup
import os

files = ['contact.html', 'appointment.html']

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find the building images
        images = soup.find_all('img', class_='block-centers__item-media-image')
        for img in images:
            img['src'] = 'Saniabuilding.avif'
            # Remove srcset as we just have one image file
            if 'srcset' in img.attrs:
                del img['srcset']
            if 'sizes' in img.attrs:
                del img['sizes']
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Updated building image in {filename}")
