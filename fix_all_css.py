import os
import re

# 第一頁的 CSS 和頁尾模板
BASE_CSS = r"""        :root {
            --bg-color: #F8F6F2;
            --text-main: #1A1A1A;
            --text-sub: #666666;
            --brand-red: #E63946;
            --border-color: #E0E0E0;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Noto Sans TC', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            overflow-x: hidden;
        }
        a { text-decoration: none; color: inherit; }

        header {
            position: fixed;
            top: 0; left: 0; width: 100%;
            padding: 20px 40px;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(248, 246, 242, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }
        .nav-logo { height: 36px; width: auto; }
        .nav-links a {
            margin-left: 30px;
            font-size: 0.8rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 300;
            color: var(--text-sub);
            transition: color 0.3s;
        }
        .nav-links a:hover { color: var(--brand-red); }
        .nav-links a.active { color: #C45C64; font-weight: 500; }
        .nav-links a.pdf-link {
            background: var(--brand-red);
            color: #fff;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.75rem;
        }
        .nav-links a.pdf-link:hover { background: #c12d38; }

        footer {
            padding: 60px 40px;
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fff;
        }
        .footer-links a { margin-left: 30px; font-size: 0.8rem; color: var(--text-sub); }

        .designer-footer {
            padding: 40px;
            background: #1A1A1A;
            color: #999;
            text-align: center;
            font-size: 0.85rem;
            line-height: 2;
        }
        .designer-footer a {
            color: #fff;
            text-decoration: none;
        }
        .designer-footer a:hover { color: var(--brand-red); }

        @media (max-width: 768px) {
            header { padding: 15px 20px; }
            .nav-links a { margin-left: 15px; font-size: 0.7rem; letter-spacing: 1px; }
            footer { flex-direction: column; gap: 20px; text-align: center; }
            .footer-links a { margin-left: 15px; }
        }"""

pages = [
    (r"F:\客戶委託專案\昇銓建材\website\第一頁(1).html", True),
    (r"F:\客戶委託專案\昇銓建材\website\官方影片\index.html", False),
    (r"F:\客戶委託專案\昇銓建材\website\全系列產品\AI圖形製作(3).html", False),
    (r"F:\客戶委託專案\昇銓建材\website\產品目錄\index.html", False),
    (r"F:\客戶委託專案\昇銓建材\website\經銷商\index.html", False),
    (r"F:\客戶委託專案\昇銓建材\website\聯絡我們\index.html", False),
]
for i in range(1, 36):
    pages.append((f"F:\\客戶委託專案\\昇銓建材\\website\\產品目錄\\{i}\\{i}.html", False))

for fp, is_home in pages:
    if not os.path.exists(fp):
        print(f"SKIP: {fp} not found")
        continue

    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it's the home page, keep its full CSS
    if is_home:
        continue

    # Replace the style block's shared CSS (header/footer/nav/designer)
    # Find and replace the style section
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        print(f"NO STYLE: {os.path.basename(fp)}")
        continue

    # Extract the existing page-specific CSS (everything not in shared)
    existing_css = style_match.group(1)

    # Replace the header/footer/nav/designer CSS block
    new_content = re.sub(
        r':root \{.*?@media.*?\}',
        BASE_CSS,
        existing_css,
        flags=re.DOTALL
    )

    content = content[:style_match.start(1)] + new_content + content[style_match.end(1):]

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"FIXED CSS: {os.path.basename(fp)}")

print("\nDone.")
