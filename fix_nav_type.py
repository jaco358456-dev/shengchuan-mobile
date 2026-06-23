import os
import re

base_dir = r"F:/工作區/昇銓手機版"

# 需要修改的檔案列表
files_to_fix = [
    "index.html",
    "全系列產品/index.html",
    "官方影片/index.html",
    "經銷商/index.html",
    "聯絡人/index.html",
    "聯絡我們/index.html",
]

# 產品目錄的 35 個產品頁
for i in range(1, 36):
    files_to_fix.append(f"產品目錄/{i}/index.html")

# 產品目錄總頁
files_to_fix.append("產品目錄/index.html")

# 要替換的兩組 pattern（導覽列的紅色按鈕 + 漢堡選單內的按鈕）
replacements = [
    # 導覽列上的紅色按鈕
    (r'<a href="電子書目錄/電子書目錄\.pdf"[^>]*class="pdf-link"[^>]*>型錄</a>', 
     '<a href="聯絡我們/index.html" class="pdf-link">聯絡我們</a>'),
    # 導覽列上的紅色按鈕（有 style 的變體）
    (r'<a href="電子書目錄/電子書目錄\.pdf"[^>]*class="pdf-link"[^>]*style="[^"]*">型錄</a>',
     '<a href="聯絡我們/index.html" class="pdf-link" style="background:var(--brand-red);color:#fff;padding:6px 12px;border-radius:20px;font-size:0.65rem;">型錄</a>'),
    # 漢堡選單內的「下載型錄」
    (r'<a href="電子書目錄/電子書目錄\.pdf"[^>]*class="mobile-nav-pdf-link"[^>]*>下載型錄</a>',
     '<a href="聯絡我們/index.html" class="mobile-nav-pdf-link" onclick="toggleNav()">聯絡我們</a>'),
    # 漢堡選單內的「下載型錄」（有 style 的變體）
    (r'<a href="電子書目錄/電子書目錄\.pdf"[^>]*class="mobile-nav-pdf-link"[^>]*style="[^"]*">下載型錄</a>',
     '<a href="聯絡我們/index.html" style="display:block;text-align:center;background:var(--brand-red);color:#fff;padding:14px;border-radius:25px;font-size:0.9rem;" onclick="toggleNav()">聯絡我們</a>'),
]

# 需要修正的 href（相對於不同頁面的路徑）
href_replacements = {
    "index.html": "聯絡我們/index.html",
    "全系列產品/index.html": "../聯絡我們/index.html",
    "官方影片/index.html": "../聯絡我們/index.html",
    "經銷商/index.html": "../聯絡我們/index.html",
    "聯絡人/index.html": "../聯絡我們/index.html",
    "聯絡我們/index.html": "index.html",  # 自己的頁面用相對路徑
    "產品目錄/index.html": "../聯絡我們/index.html",
}

count = 0
for rel_path in files_to_fix:
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"⚠️ 檔案不存在: {rel_path}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # 套用替換
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    # 如果是產品目錄的 sub-pages，href 已經是 "../聯絡我們/index.html"，不用改
    
    # 如果是其他頁面，需要修正 href
    if rel_path in href_replacements:
        target_href = href_replacements[rel_path]
        content = re.sub(
            r'href="電子書目錄/電子書目錄\.pdf"(?![^>]*class="ebook-btn")',
            f'href="{target_href}"',
            content
        )
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ {rel_path}")
        count += 1
    else:
        print(f"- {rel_path}（無變更）")

print(f"\n全部完成！共修改 {count} 個檔案")
