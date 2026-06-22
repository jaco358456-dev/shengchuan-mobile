import os

# All pages that need the designer footer
files_to_fix = [
    r"F:\客戶委託專案\昇銓建材\website\第一頁(1).html",
    r"F:\客戶委託專案\昇銓建材\website\官方影片\index.html",
    r"F:\客戶委託專案\昇銓建材\website\全系列產品\AI圖形製作(3).html",
    r"F:\客戶委託專案\昇銓建材\website\產品目錄\index.html",
    r"F:\客戶委託專案\昇銓建材\website\經銷商\index.html",
    r"F:\客戶委託專案\昇銓建材\website\聯絡我們\index.html",
]

for i in range(1, 36):
    files_to_fix.append(f"F:\\客戶委託專案\\昇銓建材\\website\\產品目錄\\{i}\\{i}.html")

designer_html = """
    <!-- 網站設計 -->
    <div class="designer-footer">
        <p>本網站由 <a href="https://www.tiktok.com/@zz489320" target="_blank">刷個存在感</a> 設計製作</p>
        <p>TikTok：@zz489320｜電話：0968 527 968</p>
    </div>"""

designer_css = """
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
        .designer-footer a:hover { color: var(--brand-red); }"""

count = 0
for fp in files_to_fix:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has designer-footer
    if 'designer-footer' in content:
        print(f"SKIP (already done): {os.path.basename(fp)}")
        continue

    # Add designer HTML before </body>
    if '</body>' in content:
        content = content.replace('</body>', designer_html + '\n</body>')

    # Add designer CSS before </style>
    if '</style>' in content:
        content = content.replace('</style>', designer_css + '\n    </style>')

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"FIXED: {os.path.basename(fp)}")

print(f"\nDone. Added designer footer to {count} files.")
