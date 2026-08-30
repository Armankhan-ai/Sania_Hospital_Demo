import os
from bs4 import BeautifulSoup
import hashlib
import re

def main():
    base_dir = r"e:\Snaiya_Hospital"
    css_dir = os.path.join(base_dir, "assets", "css")
    js_dir = os.path.join(base_dir, "assets", "js")
    
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)

    files = ['Index.html', 'about.html', 'contact.html', 'appointment.html']
    
    seen_css = set()
    seen_js = set()
    
    main_css_path = os.path.join(css_dir, "main.css")
    main_js_path = os.path.join(js_dir, "main.js")
    
    all_css_content = []
    all_js_content = []

    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"Skipping {filename} - not found.")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_html = f.read()
            
        soup = BeautifulSoup(raw_html, 'html.parser')
        
        # Regex replacement is safer than str(tag) replacement because bs4 normalizes attributes (e.g. single vs double quotes)
        # We will iterate through tags and carefully remove them via regex or just use BS4 to output the html, 
        # but the user said "design me koi change nhi hona chahiye" so preserving html exactly might be better. 
        # Actually, using BeautifulSoup to modify and then prettify/output is the standard way to do this.
        # Let's extract them using BeautifulSoup and write back the soup.
        
        for style in soup.find_all('style'):
            if style.string:
                content = style.string.strip()
                if content:
                    h = hashlib.md5(content.encode()).hexdigest()
                    if h not in seen_css:
                        seen_css.add(h)
                        all_css_content.append(content)
            style.decompose()

        for script in soup.find_all('script'):
            if not script.has_attr('src'):
                if script.string:
                    content = script.string.strip()
                    if content:
                        h = hashlib.md5(content.encode()).hexdigest()
                        if h not in seen_js:
                            seen_js.add(h)
                            all_js_content.append(content)
                script.decompose()

        # Add the links if not already present
        if soup.head:
            existing_link = soup.head.find('link', href='assets/css/main.css')
            if not existing_link:
                new_link = soup.new_tag('link', rel='stylesheet', href='assets/css/main.css')
                soup.head.append(new_link)
                
        if soup.body:
            existing_script = soup.body.find('script', src='assets/js/main.js')
            if not existing_script:
                new_script = soup.new_tag('script', src='assets/js/main.js')
                soup.body.append(new_script)

        # We will use formatter=None to avoid bs4 transforming HTML entities unnecessarily
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Refactored {filename}")

    with open(main_css_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(all_css_content))
    print(f"Created {main_css_path} with {len(all_css_content)} chunks.")

    with open(main_js_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(all_js_content))
    print(f"Created {main_js_path} with {len(all_js_content)} chunks.")

if __name__ == '__main__':
    main()
