import os, re

def fix_css(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if style has double closing tags
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        return False
    
    css = style_match.group(1)
    
    # Check if there's a stray </style> inside
    inner = css.replace('</style>', '').replace('<style>', '')
    if len(inner) < len(css):
        # Has stray closing tags
        css = inner.strip()
        content = content[:style_match.start(1)] + css + content[style_match.end(1):]
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    # Check if @media exists
    if '@media' not in css:
        # Add responsive styles before </style>
        responsive = '''
        @media (max-width: 768px) {
            header { padding: 15px 20px; }
            .nav-links a { margin-left: 15px; font-size: 0.7rem; letter-spacing: 1px; }
            footer { flex-direction: column; gap: 20px; text-align: center; }
            .footer-links a { margin-left: 15px; }
        }'''
        content = content.replace('</style>', responsive + '\n    </style>')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

pages = [
    r"F:\客戶委託專案\昇銓建材\website\官方影片\index.html",
    r"F:\客戶委託專案\昇銓建材\website\經銷商\index.html",
    r"F:\客戶委託專案\昇銓建材\website\聯絡我們\index.html",
]

for i in range(1, 36):
    pages.append(f"F:\\客戶委託專案\\昇銓建材\\website\\產品目錄\\{i}\\{i}.html")

fixed = 0
for fp in pages:
    if os.path.exists(fp):
        if fix_css(fp):
            print(f"FIXED: {os.path.basename(fp)}")
            fixed += 1
        else:
            print(f"OK: {os.path.basename(fp)}")
    else:
        print(f"MISSING: {os.path.basename(fp)}")

print(f"\nTotal fixed: {fixed}")
