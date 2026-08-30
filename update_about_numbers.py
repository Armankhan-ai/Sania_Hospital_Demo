import os
from bs4 import BeautifulSoup

filename = 'about.html'
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # We want to replace the block-why-us section completely with the new stats design.
    why_us_section = soup.find('section', class_='block-why-us')
    if why_us_section:
        new_html = """
        <section class="block-why-us" data-theme="default" style="padding-top: 5rem; padding-bottom: 5rem;">
            <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1rem; text-align: center;">
                <h2 style="color: var(--wp--preset--color--base); font-size: 2.5rem; margin-bottom: 1rem;">Sania Hospital in numbers</h2>
                <p style="font-size: 1.2rem; color: #555; max-width: 800px; margin: 0 auto 3rem auto;">
                    NABH accredited care, trusted by families across Alwar district and powered by dedicated medical talent.
                </p>
                
                <div style="display: grid; gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); text-align: left;">
                    
                    <!-- 1 -->
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">100</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">beds</h3>
                        <p style="color: #666; font-size: 0.95rem;">Total bedded multispecialty hospital with all modern facilities</p>
                    </div>

                    <!-- 2 -->
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">2004</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">year established</h3>
                        <p style="color: #666; font-size: 0.95rem;">Serving the community since our founding</p>
                    </div>

                    <!-- 3 -->
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">4</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">operation theaters</h3>
                        <p style="color: #666; font-size: 0.95rem;">Fully equipped operation theaters for surgical procedures</p>
                    </div>
                    
                    <!-- 4 -->
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">25</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">ICU beds</h3>
                        <p style="color: #666; font-size: 0.95rem;">Well-equipped ICU beds for critical patient care</p>
                    </div>

                    <!-- 5 -->
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">2019</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">NABH accreditation</h3>
                        <p style="color: #666; font-size: 0.95rem;">NABH entry level accredited hospital, June 2019 to June 2021</p>
                    </div>

                    <!-- 6 -->
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">24/7</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">emergency services</h3>
                        <p style="color: #666; font-size: 0.95rem;">Round the clock emergency and trauma care services</p>
                    </div>

                    <!-- 7 -->
                    <div style="background: #f8f9fa; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                        <div style="font-size: 3rem; font-weight: bold; color: var(--wp--preset--color--base); margin-bottom: 0.5rem;">1</div>
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem;">dialysis center</h3>
                        <p style="color: #666; font-size: 0.95rem;">Dedicated, well-equipped dialysis center for renal patients</p>
                    </div>

                </div>
            </div>
        </section>
        """
        new_soup = BeautifulSoup(new_html, 'html.parser')
        why_us_section.replace_with(new_soup)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Updated about.html stats")
