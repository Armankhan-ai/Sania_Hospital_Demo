import re
with open('Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'(<a[^>]*class=\"[^\"]*block-header__logo[^\"]*\"[^>]*>.*?</a>)', html, flags=re.IGNORECASE | re.DOTALL)
if match:
    print('Header logo:')
    print(match.group(1))

match_footer = re.search(r'(<a[^>]*class=\"[^\"]*block-footer__logo[^\"]*\"[^>]*>.*?</a>)', html, flags=re.IGNORECASE | re.DOTALL)
if match_footer:
    print('\nFooter logo:')
    print(match_footer.group(1))
