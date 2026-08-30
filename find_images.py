from bs4 import BeautifulSoup

with open('contact.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
images = soup.find_all('img')
for img in images:
    print(img.get('class'), img.get('src'))
