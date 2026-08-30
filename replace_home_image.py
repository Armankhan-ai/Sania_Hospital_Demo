from bs4 import BeautifulSoup

filename = 'Index.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()
    
soup = BeautifulSoup(content, 'html.parser')

# Find the specific image by part of its URL
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'be7a40e718687433c4ac9efb877e969125f9152e' in src:
        img['src'] = 'Saniabuilding.avif'
        if 'srcset' in img.attrs:
            del img['srcset']
        if 'sizes' in img.attrs:
            del img['sizes']

with open(filename, 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print("Updated the image on the home page.")
