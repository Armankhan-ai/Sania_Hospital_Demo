import os
from bs4 import BeautifulSoup

def redesign_about():
    with open('about.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Add custom styles for hover effects and responsive tweaks
    style_tag = soup.new_tag('style')
    style_tag.string = """
    .stat-card {
        flex: 1 1 300px;
        max-width: 350px;
        background: #ffffff;
        padding: 2.5rem 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 1px solid rgba(26, 18, 110, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .stat-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(26, 18, 110, 0.15);
    }
    .block-hero-redesigned {
        position: relative;
        height: 480px;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    .block-hero-redesigned__inner {
        position: relative;
        z-index: 10;
        text-align: center;
        max-width: 900px;
        padding: 0 20px;
    }
    .block-hero-redesigned__bg {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 1;
    }
    .block-hero-redesigned__overlay {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(0,0,0,0.7) 0%, rgba(26,18,110,0.4) 100%);
        z-index: 2;
    }
    .block-hero-redesigned img {
        width: 100%; height: 100%; object-fit: cover;
    }
    """
    soup.head.append(style_tag)

    # 1. Redesign Hero Section
    old_hero = soup.find('section', class_='block-hero')
    if old_hero:
        new_hero_html = """
        <section class="block-hero-redesigned">
            <div class="block-hero-redesigned__bg">
                <div class="block-hero-redesigned__overlay"></div>
                <img src="operation.png" alt="Sania Hospital Operation" />
            </div>
            <div class="block-hero-redesigned__inner">
                <h1 style="color: #ffffff; font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 700; margin-bottom: 1rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">About Us</h1>
                <p style="color: #f0f3f7; font-size: clamp(1.1rem, 2vw, 1.3rem); line-height: 1.6; max-width: 700px; margin: 0 auto; text-shadow: 0 1px 3px rgba(0,0,0,0.3);">Driven by care. Powered by trust. A multi & super speciality hospital with a relentless passion for patient safety.</p>
            </div>
        </section>
        """
        new_hero = BeautifulSoup(new_hero_html, 'html.parser')
        old_hero.replace_with(new_hero)

    # 2. Redesign Stats Section
    why_us = soup.find('section', class_='block-why-us')
    if why_us:
        why_us['style'] = "padding-top: 5rem; padding-bottom: 5rem; background-color: #fafbfc;"
        
        # Reduce margin below section heading
        h2 = why_us.find('h2')
        if h2:
            h2['style'] = "color: var(--wp--preset--color--base); font-size: clamp(2rem, 4vw, 2.5rem); margin-bottom: 0.5rem; font-weight: 700;"
        p = why_us.find('p')
        if p:
            p['style'] = "font-size: 1.15rem; color: #555; max-width: 800px; margin: 0 auto 2.5rem auto; line-height: 1.6;"
            
        # Change grid to flexbox for centering the last row
        grid = why_us.find('div', style=lambda v: v and 'display: grid' in v)
        if grid:
            grid['style'] = "display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; max-width: 1200px; margin: 0 auto;"
            
            # Add stat-card class to each card
            cards = grid.find_all('div', recursive=False)
            for card in cards:
                card['class'] = card.get('class', []) + ['stat-card']
                # Remove inline background/padding/shadow so CSS class takes over
                card['style'] = ""
                # Adjust h3 and numbers
                num = card.find('div')
                if num:
                    num['style'] = "font-size: 3rem; font-weight: 800; color: var(--wp--preset--color--base); margin-bottom: 0.2rem; line-height: 1;"
                h3 = card.find('h3')
                if h3:
                    h3['style'] = "font-size: 1.1rem; font-weight: 600; margin-bottom: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px;"
                desc = card.find('p')
                if desc:
                    desc['style'] = "color: #666; font-size: 0.9rem; line-height: 1.5; margin: 0;"

    # 3. CTA Section
    cta = soup.find(lambda tag: tag.name == 'section' and 'Ready to Book an Appointment?' in tag.text and 'block-why-us' not in tag.get('class', []))
    if cta:
        cta['style'] = "padding: 5rem 1rem; text-align: center; background-color: var(--wp--preset--color--violet-50); border-top: 1px solid rgba(26,18,110,0.08);"
        h2_cta = cta.find('h2')
        if h2_cta:
            h2_cta['style'] = "margin-bottom: 1.5rem; color: var(--wp--preset--color--base); font-size: clamp(1.8rem, 3vw, 2.2rem); font-weight: 700;"

    # 4. Footer Section
    # Remove background video/image from footer in about.html
    footer_video = soup.find('figure', class_='block-footer__video')
    if footer_video:
        footer_video.decompose()
        
    footer = soup.find('footer', class_='block-footer')
    if footer:
        # Give footer a clean solid background
        footer['style'] = "background-color: var(--wp--preset--color--base); color: white;"
        
        # Adjust footer main to have better column spacing
        footer_main = footer.find('div', class_='block-footer__main')
        if footer_main:
            footer_main['style'] = "padding-top: 4rem; padding-bottom: 3rem;"
            
        footer_bottom = footer.find('div', class_='block-footer__bottom')
        if footer_bottom:
            footer_bottom['style'] = "border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem; margin-top: 2rem;"

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Redesign applied successfully.")

if __name__ == '__main__':
    redesign_about()
