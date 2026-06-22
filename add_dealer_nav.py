import os

# List of HTML files to update
files_to_fix = [
    r"F:\客戶委託專案\昇銓建材\website\第一頁(1).html",
    r"F:\客戶委託專案\昇銓建材\website\官方影片\index.html",
    r"F:\客戶委託專案\昇銓建材\website\全系列產品\AI圖形製作(3).html",
    r"F:\客戶委託專案\昇銓建材\website\產品目錄\index.html",
    r"F:\客戶委託專案\昇銓建材\website\聯絡我們\index.html",
    r"F:\客戶委託專案\昇銓建材\website\經銷商\index.html",
]

# Also add to all 35 product pages
for i in range(1, 36):
    files_to_fix.append(f"F:\\客戶委託專案\\昇銓建材\\website\\產品目錄\\{i}\\{i}.html")

for fp in files_to_fix:
    if not os.path.exists(fp):
        print(f"SKIP: {fp} not found")
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # For home page
    if '第一頁(1).html' in fp:
        old = '            <a href="產品目錄/index.html">產品目錄</a>'
        new = '''            <a href="產品目錄/index.html">產品目錄</a>
            <a href="經銷商/index.html">全台經銷商</a>'''
        if old in content:
            content = content.replace(old, new)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"FIXED: {os.path.basename(fp)}")

    # For other sub-pages
    elif '第一頁(1).html' in fp or '聯絡我們' in fp:
        old = '<a href="../產品目錄/index.html">產品目錄</a>'
        new = '''<a href="../產品目錄/index.html">產品目錄</a>
            <a href="../經銷商/index.html">全台經銷商</a>'''
        if old in content:
            content = content.replace(old, new)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"FIXED: {os.path.basename(fp)}")
    else:
        # Product pages (1-35)
        old = '<a href="../產品目錄/index.html">產品目錄</a>'
        new = '''<a href="../產品目錄/index.html">產品目錄</a>
            <a href="../經銷商/index.html">全台經銷商</a>'''
        if old in content:
            content = content.replace(old, new)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"FIXED: {os.path.basename(fp)}")

print("Done.")
