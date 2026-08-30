import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

new_nav_html = '''<nav class="block-header__nav">
			<ul id="menu-primary-navigation" class="block-header__nav-list">
<li class="menu-item"><a href="Index.html">Home</a></li>
<li class="menu-item"><a href="#about">About</a></li>
<li class="menu-item"><a href="#specialities">Departments</a></li>
<li class="menu-item"><a href="#gallery">Gallery</a></li>
<li class="menu-item"><a href="contact.html">Contact</a></li>
<li class="-mobile menu-item"><a href="appointment.html" target="_self">Book Appointment</a></li>
</ul>
		</nav>'''

new_overlay_nav_html = '''<nav class="block-header__overlay-nav">
				<ul id="menu-primary-navigation-1" class="block-header__overlay-nav-list">
<li class="menu-item"><a href="Index.html">Home</a></li>
<li class="menu-item"><a href="#about">About</a></li>
<li class="menu-item"><a href="#specialities">Departments</a></li>
<li class="menu-item"><a href="#gallery">Gallery</a></li>
<li class="menu-item"><a href="contact.html">Contact</a></li>
<li class="-mobile menu-item"><a href="appointment.html" target="_self">Book Appointment</a></li>
</ul>
			</nav>'''

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix block-header__nav
    nav_pattern = re.compile(r'<nav class="block-header__nav">.*?</nav>', re.IGNORECASE | re.DOTALL)
    content = nav_pattern.sub(new_nav_html, content)
    
    # Fix block-header__overlay-nav
    overlay_nav_pattern = re.compile(r'<nav class="block-header__overlay-nav">.*?</nav>', re.IGNORECASE | re.DOTALL)
    content = overlay_nav_pattern.sub(new_overlay_nav_html, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Fixed {filename}')
