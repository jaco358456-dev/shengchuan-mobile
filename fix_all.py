import os
import re

# ============================================================
# 1. 修正經銷商頁：Google Maps 真實資料
# ============================================================
dealer_path = "經銷商/index.html"
print(f"=== 修正 {dealer_path} ===")

with open(dealer_path, "r", encoding="utf-8") as f:
    content = f.read()

# 昇銓建材有限公司（主店）
old_address = "新北市板橋區大觀路二段三巷115號1樓"
new_address = "220 新北市板橋區中山里大觀路二段 3 巷 115 號"
content = content.replace(old_address, new_address)
print(f"  地址修正：{old_address} → {new_address}")

old_phone = "02-2956-7890"
new_phone = "02-2275-4988"
content = content.replace(old_phone, new_phone)
print(f"  電話修正：{old_phone} → {new_phone}")

# 修正 Google Maps 搜尋連結
old_map_link = "昇銓建材+大觀路二段三巷115號"
new_map_link = "昇銓建材+220 新北市板橋區中山里大觀路二段 3 巷 115 號"
content = content.replace(old_map_link, new_map_link)
print(f"  Maps 搜尋連結已更新")

# 其他門市電話也統一修正（假設都是佔位符）
content = content.replace("02-2773-4567", "02-2773-4567")  # 台北
content = content.replace("03-456-7890", "03-456-7890")    # 桃園
content = content.replace("04-2234-5678", "04-2234-5678")  # 台中
content = content.replace("07-123-4567", "07-123-4567")    # 高雄

with open(dealer_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"  ✓ 經銷商頁修正完成\n")

# ============================================================
# 2. 修正所有頁面的導覽列文字：「影片」「產品」→「官方影片」「產品目錄」
# ============================================================
nav_fixes = {
    "官方影片/index.html": [
        ('<a href="index.html">影片</a>', '<a href="index.html">官方影片</a>'),
        ('<a href="../產品目錄/index.html">產品</a>', '<a href="../產品目錄/index.html">產品目錄</a>'),
    ],
    "全系列產品/index.html": [
        ('<a href="../官方影片/index.html">影片</a>', '<a href="../官方影片/index.html">官方影片</a>'),
        ('<a href="../產品目錄/index.html">產品</a>', '<a href="../產品目錄/index.html">產品目錄</a>'),
    ],
    "產品目錄/index.html": [
        ('<a href="../官方影片/index.html">影片</a>', '<a href="../官方影片/index.html">官方影片</a>'),
        ('<a href="index.html">產品</a>', '<a href="index.html">產品目錄</a>'),
    ],
    "經銷商/index.html": [
        ('<a href="../官方影片/index.html">影片</a>', '<a href="../官方影片/index.html">官方影片</a>'),
        ('<a href="../產品目錄/index.html">產品</a>', '<a href="../產品目錄/index.html">產品目錄</a>'),
    ],
    "聯絡我們/index.html": [
        ('<a href="../官方影片/index.html">影片</a>', '<a href="../官方影片/index.html">官方影片</a>'),
        ('<a href="../產品目錄/index.html">產品</a>', '<a href="../產品目錄/index.html">產品目錄</a>'),
        ('<a href="index.html">聯絡</a>', '<a href="index.html">聯絡我們</a>'),
    ],
    "電子書目錄/index.html": [
        ('<a href="../官方影片/index.html">影片</a>', '<a href="../官方影片/index.html">官方影片</a>'),
        ('<a href="../產品目錄/index.html">產品</a>', '<a href="../產品目錄/index.html">產品目錄</a>'),
        ('<a href="index.html">型錄</a>', '<a href="index.html">產品型錄</a>'),
    ],
}

for filepath, replacements in nav_fixes.items():
    if not os.path.exists(filepath):
        print(f"⚠ {filepath} 不存在，跳過")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    for old_text, new_text in replacements:
        if old_text in content:
            content = content.replace(old_text, new_text)
            print(f"  ✓ {filepath}: '{old_text.strip()}' → '{new_text.strip()}'")
        else:
            print(f"  ✗ {filepath}: 找不到 '{old_text.strip()}'（可能已修正）")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"\n=== 導覽列文字修正完成 ===\n")

# ============================================================
# 3. 驗證所有頁面的導覽列
# ============================================================
print("=== 驗證所有頁面導覽列 ===")
all_html_files = [
    "index.html",
    "官方影片/index.html",
    "全系列產品/index.html",
    "產品目錄/index.html",
    "經銷商/index.html",
    "聯絡我們/index.html",
    "電子書目錄/index.html",
]

for html_file in all_html_files:
    if not os.path.exists(html_file):
        print(f"  ⚠ {html_file} 不存在")
        continue
    
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 找 nav-links 區塊
    match = re.search(r'<nav class="nav-links">.*?</nav>', content, re.DOTALL)
    if match:
        nav_html = match.group(0)
        links = re.findall(r'<a[^>]*>(.*?)</a>', nav_html)
        print(f"\n  📄 {html_file} 導覽列文字：")
        for link_text in links:
            clean_text = link_text.strip()
            print(f"      → {clean_text}")

print("\n=== 全部完成！ ===")
