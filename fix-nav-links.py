import re
from pathlib import Path

base = Path(r"F:\工作區\昇銓手機版")

for cat_num in range(1, 36):
    html = base / str(cat_num) / "index.html"
    if not html.exists():
        continue
    
    content = html.read_text(encoding="utf-8")
    
    # 上一分類連結修正
    if cat_num > 1:
        prev = str(cat_num - 1)
        content = content.replace(f'href="../{prev}/"', f'href="../{prev}/index.html"')
    
    # 下一分類連結修正
    if cat_num < 35:
        nxt = str(cat_num + 1)
        content = content.replace(f'href="../{nxt}/"', f'href="../{nxt}/index.html"')
    
    html.write_text(content, encoding="utf-8")

print("Done - all navigation links fixed")