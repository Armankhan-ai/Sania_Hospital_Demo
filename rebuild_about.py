import os
from bs4 import BeautifulSoup

with open('Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

main_tag = soup.find('main', id='main')
if main_tag:
    main_tag.clear()
    
    about_html = """
    <div class="wp-site-blocks">
        <section class="block-hero" data-theme="dark">
            <div class="block-hero__inner">
                <div class="block-hero__content">
                    <h1 class="block-hero__heading">About us</h1>
                    <p class="block-hero__description">Driven by care. Powered by trust. A multi & super speciality hospital with a relentless passion for patient safety.</p>
                </div>
            </div>
            <figure class="block-hero__video">
                <img src="Saniabuilding.avif" alt="Sania Hospital Building" style="width:100%; height:100%; object-fit:cover; opacity: 0.6;" />
            </figure>
        </section>
        
        <section class="block-why-us" data-theme="default" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1rem; text-align: center;">
                <h2 style="color: var(--wp--preset--color--base); font-size: 2.5rem; margin-bottom: 1rem;">Sania Hospital in numbers</h2>
                <p style="font-size: 1.2rem; color: #555; max-width: 800px; margin: 0 auto 3rem auto;">
                    We are delivering advanced multispecialty healthcare to increase access to much-needed critical care for the people of Alwar.<br><br>
                    NABH accredited care, trusted by families across Alwar district and powered by dedicated medical talent.
                </p>
                
                <div style="display: grid; gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); text-align: left;">
                    
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">100</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">beds</h3>
                        <p style="color: #666; font-size: 0.95rem;">Total bedded multispecialty hospital with all modern facilities</p>
                    </div>

                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">2004</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">year established</h3>
                        <p style="color: #666; font-size: 0.95rem;">Serving the community since our founding</p>
                    </div>

                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">4</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">operation theaters</h3>
                        <p style="color: #666; font-size: 0.95rem;">Fully equipped operation theaters for surgical procedures</p>
                    </div>
                    
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">25</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">ICU beds</h3>
                        <p style="color: #666; font-size: 0.95rem;">Well-equipped ICU beds for critical patient care</p>
                    </div>

                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">2019</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">NABH accreditation</h3>
                        <p style="color: #666; font-size: 0.95rem;">NABH entry level accredited hospital, June 2019 to June 2021</p>
                    </div>

                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">24/7</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">emergency services</h3>
                        <p style="color: #666; font-size: 0.95rem;">Round the clock emergency and trauma care services</p>
                    </div>

                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">1</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">dialysis center</h3>
                        <p style="color: #666; font-size: 0.95rem;">Dedicated, well-equipped dialysis center for renal patients</p>
                    </div>

                </div>
            </div>
        </section>
        
        <section style="padding: 4rem 1rem; text-align: center; background-color: var(--wp--preset--color--violet-50);">
            <div style="max-width: 800px; margin: 0 auto;">
                <h2 style="margin-bottom: 1.5rem; color: var(--wp--preset--color--base);">Ready to Book an Appointment?</h2>
                <div style="display: flex; gap: 1rem; justify-content: center;">
                    <a href="appointment.html" style="background: var(--wp--preset--color--base); color: white; padding: 1rem 2rem; border-radius: 30px; text-decoration: none; font-weight: bold;">Book Now</a>
                    <a href="contact.html" style="background: transparent; border: 2px solid var(--wp--preset--color--base); color: var(--wp--preset--color--base); padding: 1rem 2rem; border-radius: 30px; text-decoration: none; font-weight: bold;">Contact Us</a>
                </div>
            </div>
        </section>
    </div>
    """
    
    new_body = BeautifulSoup(about_html, 'html.parser')
    main_tag.append(new_body)

title_tag = soup.find('title')
if title_tag:
    title_tag.string = "About Us - Sania Hospital"

nav_links = soup.find_all('a', href='#about')
for link in nav_links:
    link['href'] = 'about.html'
    link.string = 'About Us'

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Rebuilt about.html from Index.html")
