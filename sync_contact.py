from bs4 import BeautifulSoup

# Load Index.html
with open('Index.html', 'r', encoding='utf-8') as f:
    index_soup = BeautifulSoup(f, 'html.parser')

index_title = index_soup.find('title')
index_header = index_soup.find('header', class_='header wp-block-template-part')

# Load contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_soup = BeautifulSoup(f, 'html.parser')

contact_title = contact_soup.find('title')
contact_header = contact_soup.find('header', class_='header wp-block-template-part')

# Replace title
if contact_title and index_title:
    contact_title.replace_with(index_title)

# Replace header
if contact_header and index_header:
    contact_header.replace_with(index_header)

# Save contact.html
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(str(contact_soup))

print("Copied title and navbar from Index.html to contact.html")
