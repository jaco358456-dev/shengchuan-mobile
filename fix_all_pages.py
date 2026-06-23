import os
import re

base = r"F:/工作區/昇銓手機版"

# 所有需要修的 HTML
all_files = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(root, f))

fixed = 0
for fp in all_files:
    with open(fp, 'r', encoding='utf-8') as fh:
        html = fh.read()

    changed = False

    # 1. Logo 大小 32px → 24px
    if 'height: 32px' in html or "height:32px" in html:
        html = re.sub(r'(nav-logo\{\s*height:\s*)32px', r'\g<1>24px', html)
        changed = True

    # 2. 導覽列最後一個：型錄 → 聯絡我們（各種形式）
    # 形式 A: ../電子書目錄/電子書目錄.pdf
    if '電子書目錄/電子書目錄.pdf' in html:
        # 導覽列上的按鈕（header nav-links 內）
        old_a = '<a href="../電子書目錄/電子書目錄.pdf" class="pdf-link">型錄</a>'
        new_a = '<a href="../聯絡我們/index.html" class="pdf-link">聯絡我們</a>'
        if old_a in html:
            html = html.replace(old_a, new_a)
            changed = True

        # 漢堡選單內的連結（如果有）
        old_mob = '<a href="../電子書目錄/電子書目錄.pdf" style="display:block;text-align:center;background:var(--brand-red);color:#fff;padding:14px;border-radius:25px;font-size:0.9rem;" onclick="toggleNav()">下載型錄</a>'
        new_mob = '<a href="../聯絡我們/index.html" style="display:block;text-align:center;background:var(--brand-red);color:#fff;padding:14px;border-radius:25px;font-size:0.9rem;" onclick="toggleNav()">聯絡我們</a>'
        if old_mob in html:
            html = html.replace(old_mob, new_mob)
            changed = True

        # 漢堡選單內的簡短連結
        old_short = '<a href="../電子書目錄/電子書目錄.pdf" class="mobile-nav-pdf-link" onclick="toggleNav()">下載型錄</a>'
        new_short = '<a href="../聯絡我們/index.html" class="mobile-nav-pdf-link" onclick="toggleNav()">聯絡我們</a>'
        if old_short in html:
            html = html.replace(old_short, new_short)
            changed = True

    if changed:
        with open(fp, 'w', encoding='utf-8') as fh:
            fh.write(html)
        fixed += 1
        print(f"✓ {fp}")

print(f"\n修好了 {fixed} 個檔案")
