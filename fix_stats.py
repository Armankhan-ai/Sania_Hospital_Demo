import os
from bs4 import BeautifulSoup

def fix_stats_section():
    with open('about.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Update style for .stat-card
    style = soup.find('style', string=lambda t: t and '.stat-card' in t)
    if style:
        new_style = """
        .stat-card {
            flex: 1 1 320px;
            max-width: 340px;
            box-sizing: border-box;
            background: #fff;
            border-radius: 12px;
            padding: 2rem 1.5rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
            border: 1px solid rgba(26, 18, 110, 0.05);
        }
        .stat-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        }
        @media (max-width: 600px) {
            .stat-card {
                flex: 1 1 100%;
                max-width: 100%;
            }
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
        style.string = new_style

    why_us = soup.find('section', class_='block-why-us')
    if why_us:
        grid = why_us.find('div', style=lambda v: v and 'display: flex' in v)
        if grid:
            # Check if there are exactly 7 cards to append the 8th
            cards = grid.find_all('div', class_='stat-card')
            if len(cards) == 7:
                new_card_html = """
                <div class="stat-card">
                    <div style="font-size: 3rem; font-weight: 800; color: var(--wp--preset--color--base); margin-bottom: 0.2rem; line-height: 1;">50+</div>
                    <h3 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px;">Doctors</h3>
                    <p style="color: #666; font-size: 0.9rem; line-height: 1.5; margin: 0;">Dedicated specialists and medical professionals</p>
                </div>
                """
                new_card = BeautifulSoup(new_card_html, 'html.parser')
                grid.append(new_card)

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Done")

if __name__ == '__main__':
    fix_stats_section()
