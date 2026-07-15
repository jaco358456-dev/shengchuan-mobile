from pathlib import Path

base = Path(r"F:\工作區\昇銓手機版")

for cat_num in range(1, 36):
    html = base / str(cat_num) / "index.html"
    if not html.exists():
        continue
    
    content = html.read_text(encoding="utf-8")
    # 修正上一分類連結
    if cat_num == 1:
        content = content.replace('href="..//index.html"', 'href="index.html"')
    else:
        prev = str(cat_num - 1)
        content = content.replace(f'href="..//index.html"', f'href="../{prev}/index.html"')
    
    html.write_text(content, encoding="utf-8")

print("Done - all prev links fixed")