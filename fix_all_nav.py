import os
import re

# 導覽列模板
def build_nav(is_home, active_page):
    logo = '圖片區/logos/logo.png' if is_home else '../圖片區/logos/logo.png'
    home = '第一頁(1).html' if is_home else '../第一頁(1).html'
    video = '官方影片/index.html' if is_home else '../官方影片/index.html'
    style = '全系列產品/AI圖形製作(3).html' if is_home else '../全系列產品/AI圖形製作(3).html'
    catalog = '產品目錄/index.html' if is_home else '../產品目錄/index.html'
    dealer = '經銷商/index.html' if is_home else '../經銷商/index.html'
    ai = '第一頁(1).html#ai-section' if is_home else '../第一頁(1).html#ai-section'
    ambassador = '第一頁(1).html#ambassador' if is_home else '../第一頁(1).html#ambassador'
    contact = '聯絡我們/index.html' if is_home else '../聯絡我們/index.html'
    ebook = '電子書目錄/電子書目錄.pdf' if is_home else '../電子書目錄/電子書目錄.pdf'

    def active(name, page):
        cls = ' class="active"' if active_page == page else ''
        return cls

    nav = f'''    <header>
        <img src="{logo}" alt="紅螞蟻磁磚 Logo" class="nav-logo">
        <nav class="nav-links">
            <a href="{home}">首頁</a>
            <a href="{video}"{active("video", "video")}>官方影片</a>
            <a href="{style}"{active("style", "style")}>風格總覽</a>
            <a href="{catalog}"{active("catalog", "catalog")}>產品目錄</a>
            <a href="{dealer}"{active("dealer", "dealer")}>全台經銷商</a>
            <a href="{ai}"{active("ai", "ai")}>AI 虛擬代言人</a>
            <a href="{ambassador}"{active("ambassador", "ambassador")}>品牌大使</a>
            <a href="{contact}"{active("contact", "contact")}>聯絡我們</a>
            <a href="{ebook}" class="pdf-link">電子書目錄</a>
        </nav>
    </header>'''
    return nav

# 頁面分類
pages = [
    # (file, is_home, active_page)
    (r"F:\客戶委託專案\昇銓建材\website\第一頁(1).html", True, "home"),
    (r"F:\客戶委託專案\昇銓建材\website\官方影片\index.html", False, "video"),
    (r"F:\客戶委託專案\昇銓建材\website\全系列產品\AI圖形製作(3).html", False, "style"),
    (r"F:\客戶委託專案\昇銓建材\website\產品目錄\index.html", False, "catalog"),
    (r"F:\客戶委託專案\昇銓建材\website\經銷商\index.html", False, "dealer"),
    (r"F:\客戶委託專案\昇銓建材\website\聯絡我們\index.html", False, "contact"),
]

for i in range(1, 36):
    pages.append((f"F:\\客戶委託專案\\昇銓建材\\website\\產品目錄\\{i}\\{i}.html", False, "catalog"))

for fp, is_home, active_page in pages:
    if not os.path.exists(fp):
        print(f"SKIP: {fp} not found")
        continue

    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    new_nav = build_nav(is_home, active_page)

    old_header = re.search(r'<header>.*?</header>', content, re.DOTALL)
    if old_header:
        content = content[:old_header.start()] + new_nav + content[old_header.end():]
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED: {os.path.basename(fp)}")
    else:
        print(f"NO HEADER: {os.path.basename(fp)}")

print("\nDone. All navs unified based on 第一頁(1).html template.")
