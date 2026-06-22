import os
import re

pages = []
for root, dirs, files in os.walk(r"F:\客戶委託專案\昇銓建材\website"):
    for f in files:
        if f.endswith('.html'):
            pages.append(os.path.join(root, f))

count = 0
for fp in pages:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix both forms
    content = content.replace('圖片區/logos/logo.png', 'logos/logo.png')
    content = content.replace('../圖片區/logos/logo.png', '../logos/logo.png')

    if '圖片區/logos/logo.png' not in content and '../圖片區/logos/logo.png' not in content:
        # Check if anything changed
        pass
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    
    rel = fp.replace(r"F:\客戶委託專案\昇銓建材\website\\", "")
    count += 1
    print(f"FIXED: {rel}")

print(f"\nDone. Processed {count} files.")
