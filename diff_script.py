import re
import difflib

def get_block_why_us(file):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    match = re.search(r'(<section class=\"block-why-us.*?</section>)', html, flags=re.DOTALL)
    if not match: return ''
    lines = match.group(1).splitlines()
    return '\n'.join([l for l in lines if l.strip()])

orig = get_block_why_us('original.html')
curr = get_block_why_us('Index.html')

if orig and curr:
    diff = list(difflib.unified_diff(orig.splitlines(), curr.splitlines(), fromfile='original', tofile='current'))
    for line in diff:
        print(line)
