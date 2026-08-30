from bs4 import BeautifulSoup
import re

def copy_footer():
    # Read Index.html
    with open('Index.html', 'r', encoding='utf-8') as f:
        index_soup = BeautifulSoup(f, 'html.parser')
    
    # Extract footer and footer video/graphics if any that are sibling/near footer
    # Looking at typical structure, there's `<footer class="block-footer">`
    index_footer = index_soup.find('footer', class_='block-footer')
    
    # Read about.html
    with open('about.html', 'r', encoding='utf-8') as f:
        about_soup = BeautifulSoup(f, 'html.parser')
        
    about_footer = about_soup.find('footer', class_='block-footer')
    
    if index_footer and about_footer:
        # We replace the about_footer with index_footer
        about_footer.replace_with(index_footer)
        
        # Save about.html
        with open('about.html', 'w', encoding='utf-8') as f:
            f.write(str(about_soup))
        print("Footer successfully copied from Index.html to about.html.")
    else:
        print("Could not find footer in one of the files.")

if __name__ == '__main__':
    copy_footer()
