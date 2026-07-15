import re
from pathlib import Path

html = Path(r"F:\工作區\昇銓手機版\products\index.html")
content = html.read_text(encoding="utf-8")

# 把所有 href="X/index.html" 改成 href="../X/index.html"
content = re.sub(r'href="(\d+)/index.html"', r'href="../\1/index.html"', content)

html.write_text(content, encoding="utf-8")
print("Done")