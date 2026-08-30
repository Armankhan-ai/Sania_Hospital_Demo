from bs4 import BeautifulSoup

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Find the main tag
main_tag = soup.find('main', id='main')
if main_tag:
    main_tag.clear()
    
    # We will build a block-hero for About Us, followed by block-about or block-why-us
    about_html = """
    <div class="wp-site-blocks">
        <section class="block-hero" data-theme="dark">
            <div class="block-hero__inner">
                <div class="block-hero__content">
                    <h1 class="block-hero__heading">About Sania Hospital</h1>
                    <p class="block-hero__description">Where loving & caring has meant real healing since 2004.</p>
                </div>
            </div>
            <figure class="block-hero__video">
                <img src="Saniabuilding.avif" alt="Sania Hospital Building" style="width:100%; height:100%; object-fit:cover; opacity: 0.6;" />
            </figure>
        </section>
        
        <section class="block-why-us" data-theme="default" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1rem;">
                <div style="display: grid; gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <h2 style="color: var(--wp--preset--color--base); margin-bottom: 1rem;">Our History</h2>
                        <p>Established in 2004, Sania Hospital was founded by Dr. Taiyab Khan, MBBS, MD Medicine, with a vision to provide the best and most comprehensive medical care to the people of Alwar and surrounding regions.</p>
                    </div>
                    
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <h2 style="color: var(--wp--preset--color--base); margin-bottom: 1rem;">Facilities & Capacity</h2>
                        <p>We are a state-of-the-art 100-bedded multispecialty hospital. Our infrastructure includes 4 advanced operation theaters, a 25-bedded ICU with round-the-clock monitoring, a fully functional dialysis center, and an advanced trauma-care unit.</p>
                    </div>

                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <h2 style="color: var(--wp--preset--color--base); margin-bottom: 1rem;">Our Location</h2>
                        <p>Sania Hospital is centrally located to serve the community efficiently. <br><br><strong>Address:</strong><br> 249, NEB, Subhash Nagar, Shastri Nagar,<br> Alwar, Rajasthan - 301001</p>
                    </div>
                    
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <h2 style="color: var(--wp--preset--color--base); margin-bottom: 1rem;">Comprehensive Services</h2>
                        <p>Our expert medical team provides comprehensive care spanning from emergency trauma response to critical intensive care. We offer consultations across multiple specialties including a dedicated dental OPD.</p>
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

# Change title
title_tag = soup.find('title')
if title_tag:
    title_tag.string = "About Us - Sania Hospital"

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Created about.html")
