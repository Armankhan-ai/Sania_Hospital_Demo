import json
with open('Index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

footer_start = -1
for i, line in enumerate(lines):
    if '<footer data-wpr-lazyrender="1" class="footer wp-block-template-part">' in line:
        footer_start = i
        break

if footer_start != -1:
    script_end = -1
    for i in range(footer_start, len(lines)):
        if '//# sourceURL=rocket-preload-links-js-after' in lines[i]:
            script_end = i + 1 
            break
    
    if script_end != -1:
        new_lines = lines[:script_end+1]
        new_lines.extend([
            '<script id="rezonbio-scripts-js-extra">\n',
            'var rezonbioData = {"ajax_url":"https://rezonbio.com/wp-admin/admin-ajax.php","nonce":"5d12d64fed"};\n',
            '//# sourceURL=rezonbio-scripts-js-extra\n',
            '</script>\n',
            '<script data-minify="1" id="rezonbio-scripts-js" src="https://portfolio.widehue.co/rezonbio/wp-content/themes/rezonbio/assets/build/js/index.js?ver=1765180998" data-rocket-defer defer></script>\n',
            '<script id="gsap-core-js" src="https://portfolio.widehue.co/rezonbio/wp-content/themes/rezonbio/assets/vendor/gsap/gsap.min.js?ver=3.12.2" data-rocket-defer defer></script>\n',
            '<script id="gsap-scrolltrigger-js" src="https://portfolio.widehue.co/rezonbio/wp-content/themes/rezonbio/assets/vendor/gsap/scrollTrigger.min.js?ver=3.12.2" data-rocket-defer defer></script>\n',
            '<script id="gsap-splittext-js" src="https://portfolio.widehue.co/rezonbio/wp-content/themes/rezonbio/assets/vendor/gsap/SplitText.min.js?ver=3.12.2" data-rocket-defer defer></script>\n',
            '<script id="gsap-scrolltoplugin-js" src="https://portfolio.widehue.co/rezonbio/wp-content/themes/rezonbio/assets/vendor/gsap/ScrollToPlugin.min.js?ver=3.12.2" data-rocket-defer defer></script>\n',
            '</body>\n',
            '</html>\n'
        ])
        
        with open('Index.html', 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print('Cleaned up Index.html successfully. New line count:', len(new_lines))
    else:
        print('Could not find rocket-preload script')
else:
    print('Could not find footer')
