import os
import re

base_dir = r"F:/工作區/昇銓手機版"

# 所有需要修改的 HTML 檔案
files = []
for root, dirs, filenames in os.walk(base_dir):
    for f in filenames:
        if f.endswith('.html'):
            files.append(os.path.join(root, f))

count = 0
for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # 導覽列紅色按鈕：型錄 → 聯絡我們
    # 變體1：href="../電子書目錄/電子書目錄.pdf" class="pdf-link">型錄</a>
    content = re.sub(
        r'href="電子書目錄/電子書目錄\.pdf"(?![^>]*class="ebook-btn")[^>]*class="pdf-link"[^>]*>型錄</a>',
        'href="聯絡我們/index.html" class="pdf-link">聯絡我們</a>',
        content
    )
    
    # 變體2：有 style 的紅色按鈕
    content = re.sub(
        r'href="../電子書目錄/電子書目錄\.pdf"[^>]*class="pdf-link"[^>]*style="[^"]*">型錄</a>',
        'href="../聯絡我們/index.html" class="pdf-link" style="background:var(--brand-red);color:#fff;padding:6px 12px;border-radius:20px;font-size:0.65rem;">型錄</a>',
        content
    )
    
    # 漢堡選單內的「下載型錄」→「聯絡我們」
    content = re.sub(
        r'href="../電子書目錄/電子書目錄\.pdf"[^>]*class="mobile-nav-pdf-link"[^>]*>下載型錄</a>',
        'href="../聯絡我們/index.html" class="mobile-nav-pdf-link" onclick="toggleNav()">聯絡我們</a>',
        content
    )
    
    # 變體：有 style 的漢堡選單按鈕
    content = re.sub(
        r'href="../電子書目錄/電子書目錄\.pdf"[^>]*class="mobile-nav-pdf-link"[^>]*style="[^"]*">下載型錄</a>',
        'href="../聯絡我們/index.html" style="display:block;text-align:center;background:var(--brand-red);color:#fff;padding:14px;border-radius:25px;font-size:0.9rem;" onclick="toggleNav()">聯絡我們</a>',
        content
    )
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ {os.path.relpath(filepath, base_dir)}")
        count += 1
    else:
        print(f"- {os.path.relpath(filepath, base_dir)}（無變更）")

print(f"\n全部完成！共修改 {count} 個檔案")
