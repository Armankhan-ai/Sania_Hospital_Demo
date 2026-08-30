import os

files = ['Index.html', 'contact.html', 'appointment.html']
style_to_inject = "\n<style>.block-footer__credits::before { content: none !important; display: none !important; }</style>\n"

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'block-footer__credits::before' not in content:
            # Insert just before </head>
            if '</head>' in content:
                content = content.replace('</head>', style_to_inject + '</head>')
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filename}")
            else:
                print(f"</head> not found in {filename}")
