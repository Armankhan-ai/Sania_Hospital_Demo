import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

new_cta = '''<div class="block-header__cta" >
		<a href="appointment.html" target="_self" class="wp-block-button__link wp-element-button" style="background: #007bff; color: white; padding: 10px 24px; border-radius: 30px; font-weight: bold; text-decoration: none; box-shadow: 0 4px 6px rgba(0,123,255,0.3); transition: background 0.3s ease;">
			Book Appointment
		</a>
	</div>'''

for filename in files_to_update:
    filepath = os.path.join(r'e:\Snaiya_Hospital', filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match the block-header__cta div
    cta_pattern = re.compile(r'<div class="block-header__cta".*?</div>', re.IGNORECASE | re.DOTALL)
    
    # Replace it
    content = cta_pattern.sub(new_cta, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Updated CTA in {filename}')
