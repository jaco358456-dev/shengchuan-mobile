from pathlib import Path

base = Path(r"F:\工作區\昇銓手機版")

for cat_num in range(1, 36):
    html = base / str(cat_num) / "index.html"
    if not html.exists():
        continue
    
    content = html.read_text(encoding="utf-8")
    
    # 把所有 ../../products/ 改成 ../products/
    content = content.replace('../../products/', '../products/')
    
    html.write_text(content, encoding="utf-8")

print("Done - products links fixed")