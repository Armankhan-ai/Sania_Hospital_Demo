import re
import glob

def create_page(template_content, output_path, title):
    # Find <main ...> ... </main> using regex and replace its content
    main_pattern = re.compile(r'(<main[^>]*>).*?(</main>)', re.DOTALL | re.IGNORECASE)
    
    new_main_content = f'''\\1
<div class="entry-content wp-block-post-content">
<section class="block-hero" data-theme="dark" style="min-height: 60vh; display: flex; align-items: center; justify-content: center;">
<h1 style="color: #fff; text-align: center; font-size: 3rem; margin: 0;">THIS PAGE LIVE SOON..</h1>
</section>
</div>
\\2'''
    
    new_content = main_pattern.sub(new_main_content, template_content)
    
    # Update title
    title_pattern = re.compile(r'<title>.*?</title>', re.IGNORECASE)
    new_content = title_pattern.sub(f'<title>{title} - Sania Hospital</title>', new_content)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def update_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Departments link
    content = re.sub(r'href="Index\.html#specialities"', 'href="department.html"', content, flags=re.IGNORECASE)
    content = re.sub(r'href="#specialities"', 'href="department.html"', content, flags=re.IGNORECASE)
    
    # Replace Gallery link
    content = re.sub(r'href="Index\.html#gallery"', 'href="gallery.html"', content, flags=re.IGNORECASE)
    content = re.sub(r'href="#gallery"', 'href="gallery.html"', content, flags=re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Read template from contact.html
    with open(r'e:\Snaiya_Hospital\contact.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
        
    # Create new pages
    create_page(template_content, r'e:\Snaiya_Hospital\department.html', 'Departments')
    create_page(template_content, r'e:\Snaiya_Hospital\gallery.html', 'Gallery')
    
    print("Created department.html and gallery.html")
    
    # Update links in all HTML files
    html_files = glob.glob(r'e:\Snaiya_Hospital\*.html')
    for html_file in html_files:
        update_links(html_file)
        print(f"Updated links in {html_file}")

if __name__ == "__main__":
    main()
