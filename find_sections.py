from bs4 import BeautifulSoup
with open('Index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
sections = soup.find_all('section')
for i, s in enumerate(sections):
    class_name = s.get('class', [])
    text = s.text.strip()[:50].replace('\n', ' ')
    print(f"Section {i}: class={class_name}, text={text}")
