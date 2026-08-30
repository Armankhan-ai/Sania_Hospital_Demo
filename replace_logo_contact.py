import re

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Header Logo
new_header_logo = '''<a href="index.html" class="block-header__logo" aria-label="Logo">
			<img src="AA.avif" alt="Logo" style="max-height: 40px; width: auto;">
		</a>'''
html = re.sub(r'<a[^>]*class=\"[^\"]*block-header__logo[^\"]*\"[^>]*>.*?</a>', new_header_logo, html, flags=re.IGNORECASE | re.DOTALL)

# Replace Footer Logo
new_footer_logo = '''<a href="index.html" class="block-footer__logo" aria-label="Logo">
				<img src="AA.avif" alt="Sania Hospital" style="height: 32px; width: auto;">
			</a>'''
html = re.sub(r'<a[^>]*class=\"[^\"]*block-footer__logo[^\"]*\"[^>]*>.*?</a>', new_footer_logo, html, flags=re.IGNORECASE | re.DOTALL)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated contact.html")
