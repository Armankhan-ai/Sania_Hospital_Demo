import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

new_logo_html = '''<a href="Index.html" class="block-header__logo" aria-label="Logo" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">
			<img src="AA.avif" alt="Logo" style="max-height: 40px; width: auto;">
			<div style="display: flex; flex-direction: column; line-height: 1.2;">
				<span style="font-weight: bold; font-size: 1.2rem; color: var(--wp--preset--color--black, #000);">Sania Hospital</span>
				<span style="font-size: 0.75rem; color: var(--wp--preset--color--gray, #666);">Advanced Care. Compassionate Healing.</span>
			</div>
		</a>'''

new_nav_html = '''<ul id="menu-primary-navigation" class="block-header__nav-list">
<li class="menu-item"><a href="Index.html">Home</a></li>
<li class="menu-item"><a href="#about">About</a></li>
<li class="menu-item"><a href="#specialities">Departments</a></li>
<li class="menu-item"><a href="#gallery">Gallery</a></li>
<li class="menu-item"><a href="contact.html">Contact</a></li>
<li class="-mobile menu-item"><a href="appointment.html" target="_self">Book Appointment</a></li>
</ul>'''

new_overlay_nav_html = '''<ul id="menu-primary-navigation-1" class="block-header__overlay-nav-list">
<li class="menu-item"><a href="Index.html">Home</a></li>
<li class="menu-item"><a href="#about">About</a></li>
<li class="menu-item"><a href="#specialities">Departments</a></li>
<li class="menu-item"><a href="#gallery">Gallery</a></li>
<li class="menu-item"><a href="contact.html">Contact</a></li>
<li class="-mobile menu-item"><a href="appointment.html" target="_self">Book Appointment</a></li>
</ul>'''

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace logo
    logo_pattern = re.compile(r'<a href="index\.html" class="block-header__logo"[^>]*>.*?</a>', re.IGNORECASE | re.DOTALL)
    content = logo_pattern.sub(new_logo_html, content)
    
    # 2. Replace desktop nav
    nav_pattern = re.compile(r'<ul id="menu-primary-navigation" class="block-header__nav-list">.*?</ul>', re.IGNORECASE | re.DOTALL)
    content = nav_pattern.sub(new_nav_html, content)
    
    # 3. Replace mobile overlay nav
    overlay_nav_pattern = re.compile(r'<ul id="menu-primary-navigation-1" class="block-header__overlay-nav-list">.*?</ul>', re.IGNORECASE | re.DOTALL)
    content = overlay_nav_pattern.sub(new_overlay_nav_html, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Updated {filename}')
