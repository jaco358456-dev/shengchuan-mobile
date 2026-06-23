import os

dirs_to_fix = [
    "官方影片",
    "全系列產品",
    "產品目錄",
    "經銷商",
    "聯絡我們",
    "電子書目錄",
]

for d in dirs_to_fix:
    path = os.path.join(d, "index.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    old = '<a href="../官方影片/index.html">影片</a>'
    new = '<a href="../官方影片/index.html">官方影片</a>'
    if old in content:
        content = content.replace(old, new)
        print(f"FIX {d}: 影片 -> 官方影片")
    else:
        print(f"SKIP {d}: no match")
    
    old = '<a href="../產品目錄/index.html">產品</a>'
    new = '<a href="../產品目錄/index.html">產品目錄</a>'
    if old in content:
        content = content.replace(old, new)
        print(f"FIX {d}: 產品 -> 產品目錄")
    else:
        print(f"SKIP {d}: no match")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("\nDone!")