import os
import re

files_to_update = ['Index.html', 'contact.html', 'appointment.html']

new_cta = '''<div class="block-header__cta" >
    <style>
        .premium-btn {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #ffffff !important;
            padding: 12px 30px;
            border-radius: 50px;
            font-family: inherit;
            font-weight: 700;
            font-size: 0.9rem;
            letter-spacing: 1px;
            text-transform: uppercase;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 20px rgba(44, 83, 100, 0.3);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
        }
        .premium-btn::before {
            content: '';
            position: absolute;
            top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.3) 50%, rgba(255,255,255,0) 100%);
            transform: skewX(-25deg);
            transition: all 0.6s ease;
        }
        .premium-btn:hover::before {
            left: 150%;
        }
        .premium-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 25px rgba(44, 83, 100, 0.4);
        }
    </style>
    <a href="appointment.html" target="_self" class="premium-btn">
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
        
    print(f'Updated Premium CTA in {filename}')
