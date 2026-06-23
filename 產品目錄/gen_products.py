import os

product_dirs = sorted(
    [d for d in os.listdir('.') if os.path.isdir(d) and d.isdigit()],
    key=int
)

# 產品分類映射
product_info = {
    1:  {"name": "大理石紋 A", "cat": "石材系列", "desc": "天然大理紋理，展現石材原始之美，適合客廳與餐廳鋪設", "tags": ["石材", "大理石", "室內"]},
    2:  {"name": "石灰岩 B",   "cat": "石材系列", "desc": "質樸質感，營造簡約自然氛圍", "tags": ["石材", "石灰岩", "質感"]},
    3:  {"name": "花崗岩 C",   "cat": "石材系列", "desc": "堅硬耐用，適合高使用頻率空間", "tags": ["石材", "花崗岩", "耐用"]},
    4:  {"name": "板岩 D",     "cat": "石材系列", "desc": "層疊紋理，展現自然粗獷之美", "tags": ["石材", "板岩", "自然"]},
    5:  {"name": "橡木紋 E",   "cat": "木紋系列", "desc": "溫潤木紋色調，營造溫馨居家氛圍", "tags": ["木紋", "橡木", "溫馨"]},
    6:  {"name": "胡桃木紋 F", "cat": "木紋系列", "desc": "深沉木紋色調，適合現代風格空間", "tags": ["木紋", "胡桃木", "現代"]},
    7:  {"name": "松木紋 G",   "cat": "木紋系列", "desc": "明亮木紋色調，營造輕盈通透感", "tags": ["木紋", "松木", "輕盈"]},
    8:  {"name": "柚木紋 H",   "cat": "木紋系列", "desc": "高雅木紋色調，展現品味格調", "tags": ["木紋", "柚木", "高雅"]},
    9:  {"name": "純白 I",     "cat": "現代極簡", "desc": "純淨白色調，打造明亮簡約空間", "tags": ["極簡", "純白", "明亮"]},
    10: {"name": "水泥灰 J",   "cat": "現代極簡", "desc": "工業風水泥紋理，展現時髦態度", "tags": ["極簡", "水泥灰", "工業風"]},
    11: {"name": "珍珠灰 K",   "cat": "現代極簡", "desc": "柔和灰色調，營造寧靜氛圍", "tags": ["極簡", "珍珠灰", "寧靜"]},
    12: {"name": "星空黑 L",   "cat": "現代極簡", "desc": "深邃黑色調，展現沉穩氣質", "tags": ["極簡", "星空黑", "沉穩"]},
    13: {"name": "大理石拼花 M", "cat": "設計款系列", "desc": "復古拼花圖案，展現藝術氣息", "tags": ["設計", "大理石", "拼花"]},
    14: {"name": "幾何拼接 N", "cat": "設計款系列", "desc": "現代幾何圖案，營造視覺層次", "tags": ["設計", "幾何", "拼接"]},
    15: {"name": "抽象藝術 O", "cat": "設計款系列", "desc": "自由抽象圖案，展現個性風格", "tags": ["設計", "抽象", "藝術"]},
    16: {"name": "自然拼貼 P", "cat": "設計款系列", "desc": "自然元素拼貼，呈現原始美感", "tags": ["設計", "自然", "拼貼"]},
}

base_template = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | 紅螞蟻磁磚 產品詳情</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #F8F6F2;
            --text-main: #1A1A1A;
            --text-sub: #666666;
            --brand-red: #E63946;
            --card-bg: #FFFFFF;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.12);
            --radius: 12px;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        img {{ width: 100%; height: auto; display: block; }}
        body {{
            font-family: 'Noto Sans TC', sans-serif;
            background: var(--bg-color);
            color: var(--text-main);
            overflow-x: hidden;
        }}
        a {{ text-decoration: none; color: inherit; }}

        header {{
            position: fixed;
            top: 0; left: 0;
            width: 100%;
            padding: 15px 20px;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(248,246,242,0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }}
        .nav-logo {{ height: 32px; width: auto; }}
        .nav-links {{ display: flex; align-items: center; }}
        .nav-links a {{
            margin-left: 16px;
            font-size: 0.7rem;
            letter-spacing: 1px;
            text-transform: uppercase;
            font-weight: 300;
            color: var(--text-sub);
            white-space: nowrap;
        }}
        .nav-links a.pdf-link {{
            background: var(--brand-red);
            color: #fff;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.65rem;
        }}

        .hamburger {{
            display: flex;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
            z-index: 1100;
            padding: 5px;
        }}
        .hamburger span {{
            width: 25px;
            height: 2px;
            background: var(--text-main);
            border-radius: 2px;
        }}
        .hamburger.active span:nth-child(1) {{ transform: rotate(45deg) translate(5px, 5px); }}
        .hamburger.active span:nth-child(2) {{ opacity: 0; }}
        .hamburger.active span:nth-child(3) {{ transform: rotate(-45deg) translate(5px, -5px); }}

        .mobile-nav-overlay {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(248,246,242,0.98);
            z-index: 1050;
            display: flex;
            flex-direction: column;
            transform: translateY(-100%);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .mobile-nav-overlay.open {{ transform: translateY(0); }}
        .mobile-nav-header {{ padding: 60px 20px 20px; flex: 1; }}
        .mobile-nav-close {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 30px;
        }}
        .mobile-nav-back {{
            padding: 10px 20px;
            border: 1px solid var(--text-main);
            border-radius: 25px;
            font-size: 0.85rem;
        }}
        .mobile-nav-close-btn {{
            font-size: 1.5rem;
            cursor: pointer;
            padding: 10px;
            border: none;
            background: none;
        }}
        .mobile-nav-title {{
            font-size: 0.7rem;
            letter-spacing: 3px;
            color: var(--text-sub);
            margin-bottom: 15px;
            text-transform: uppercase;
        }}
        .mobile-nav-links {{ display: flex; flex-direction: column; }}
        .mobile-nav-links a {{
            display: block;
            font-size: 1.1rem;
            padding: 16px 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }}

        /* 產品主圖 */
        .product-hero {{
            margin-top: 65px;
        }}
        .product-hero img {{
            width: 100%;
            height: auto;
            display: block;
        }}

        /* 產品資訊區 */
        .product-detail {{
            padding: 24px 20px;
        }}
        .product-breadcrumb {{
            font-size: 0.7rem;
            color: var(--text-sub);
            letter-spacing: 1px;
            margin-bottom: 16px;
        }}
        .product-breadcrumb a {{
            color: var(--brand-red);
        }}
        .product-title {{
            font-size: 1.5rem;
            font-weight: 400;
            margin-bottom: 8px;
            letter-spacing: 2px;
        }}
        .product-cat {{
            font-size: 0.7rem;
            color: var(--text-sub);
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 16px;
        }}
        .product-desc {{
            font-size: 0.9rem;
            color: var(--text-sub);
            line-height: 1.8;
            margin-bottom: 20px;
        }}
        .product-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 24px;
        }}
        .product-tag {{
            display: inline-block;
            padding: 6px 14px;
            background: #f0f0f0;
            border-radius: 20px;
            font-size: 0.7rem;
            color: var(--text-sub);
            letter-spacing: 1px;
        }}

        /* 多圖展示區 */
        .gallery-section {{
            padding: 0 20px 30px;
        }}
        .gallery-title {{
            font-size: 1rem;
            font-weight: 400;
            letter-spacing: 1px;
            margin-bottom: 16px;
            padding-top: 10px;
        }}
        .gallery-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
        }}
        .gallery-item {{
            border-radius: var(--radius);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            background: var(--card-bg);
        }}
        .gallery-item img {{
            width: 100%;
            height: auto;
            display: block;
        }}
        .gallery-label {{
            padding: 10px 14px;
            font-size: 0.75rem;
            color: var(--text-sub);
            letter-spacing: 1px;
        }}

        /* 回到產品目錄 */
        .back-link {{
            display: block;
            text-align: center;
            padding: 16px 20px;
            border-top: 1px solid #E0E0E0;
            margin-top: 20px;
        }}
        .back-link a {{
            display: inline-block;
            padding: 12px 28px;
            border: 1px solid var(--text-main);
            border-radius: 25px;
            font-size: 0.85rem;
            letter-spacing: 1px;
            color: var(--text-main);
        }}

        .footer-bar {{
            padding: 30px 20px;
            border-top: 1px solid #E0E0E0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--card-bg);
        }}
        .footer-bar img:first-child {{
            height: 24px;
            width: auto;
            opacity: 0.4;
        }}
        .footer-icons {{ display: flex; gap: 12px; align-items: center; }}
        .footer-icons img {{ height: 24px; width: auto; opacity: 0.6; }}
        .designer-box {{
            padding: 24px 20px;
            background: #1A1A1A;
            color: #999;
            text-align: center;
            font-size: 0.75rem;
            line-height: 1.8;
        }}
        .designer-box a {{ color: #fff; }}
    </style>
</head>
<body>
    <!-- 導覽列 -->
    <header>
        <img src="../logos/logo.png" alt="紅螞蟻磁磚 Logo" class="nav-logo">
        <div class="hamburger" id="hamburger" onclick="toggleNav()">
            <span></span><span></span><span></span>
        </div>
        <nav class="nav-links">
            <a href="../index.html">首頁</a>
            <a href="../官方影片/index.html">官方影片</a>
            <a href="../產品目錄/index.html">產品目錄</a>
            <a href="../經銷商/index.html">經銷商</a>
            <a href="../電子書目錄/電子書目錄.pdf" class="pdf-link">型錄</a>
        </nav>
    </header>

    <!-- 導覽列覆蓋 -->
    <div class="mobile-nav-overlay" id="navOverlay">
        <div class="mobile-nav-header">
            <div class="mobile-nav-close">
                <a href="../index.html" class="mobile-nav-back" onclick="toggleNav()">← 回首頁</a>
                <button class="mobile-nav-close-btn" onclick="toggleNav()">✕</button>
            </div>
            <div class="mobile-nav-title">導航選單</div>
            <div class="mobile-nav-links">
                <a href="../index.html" onclick="toggleNav()">首頁</a>
                <a href="../官方影片/index.html" onclick="toggleNav()">官方影片</a>
                <a href="../產品目錄/index.html" onclick="toggleNav()">產品目錄</a>
                <a href="../經銷商/index.html" onclick="toggleNav()">全台經銷商</a>
                <a href="../聯絡我們/index.html" onclick="toggleNav()">聯絡我們</a>
            </div>
        </div>
        <div style="padding:20px;">
            <a href="../電子書目錄/電子書目錄.pdf" class="mobile-nav-pdf-link" style="display:block;text-align:center;background:var(--brand-red);color:#fff;padding:14px;border-radius:25px;font-size:0.9rem;" onclick="toggleNav()">下載型錄</a>
        </div>
    </div>
    <script>function toggleNav(){{document.getElementById('navOverlay').classList.toggle('open');document.getElementById('hamburger').classList.toggle('active');}}</script>

    <!-- 產品主圖 -->
     <div class="product-hero">
         <img src="{main_img}" alt="{name}">
     </div>

    <!-- 產品資訊 -->
    <div class="product-detail">
        <div class="product-breadcrumb">
            <a href="../產品目錄/index.html">產品目錄</a> / {cat} / {name}
        </div>
        <h1 class="product-title">{name}</h1>
        <div class="product-cat">{cat}</div>
        <p class="product-desc">{desc}</p>
        <div class="product-tags">
{tags}
        </div>
    </div>

    <!-- 產品多圖展示 -->
    <div class="gallery-section">
        <div class="gallery-title">產品圖片展示</div>
        <div class="gallery-grid">
{gallery}
        </div>
    </div>

    <!-- 回到產品目錄 -->
    <div class="back-link">
        <a href="../產品目錄/index.html">← 返回產品目錄</a>
    </div>

    <!-- 頁尾 -->
    <div class="footer-bar">
        <img src="../logos/logo.png" alt="紅螞蟻磁磚 Logo">
        <div class="footer-icons">
            <img src="../logos/icon-fb.png" alt="Facebook">
            <img src="../logos/icon-ig.png" alt="Instagram">
            <img src="../logos/icon-yt.png" alt="YouTube">
        </div>
    </div>
    <div class="designer-box">
        <p>本網站由 <a href="https://www.tiktok.com/@zz489320" target="_blank">刷個存在感</a> 設計製作</p>
        <p>TikTok：@zz489320｜電話：0968 527 968</p>
    </div>
</body>
</html>'''

for num in product_dirs:
    num_int = int(num)
    info = product_info.get(num_int, {"name": f"產品 {num_int}", "cat": "全系列", "desc": "紅螞蟻磁磚精選款式", "tags": ["紅螞蟻磁磚"]})
    
    # 收集產品圖片
    gallery_items = []
    
    # 先加 product0xxx.jpg（主產品圖）
    product_files = sorted([
        f for f in os.listdir(num)
        if f.startswith("product0") and f.endswith(('.jpg', '.png'))
    ])
    for pf in product_files:
        gallery_items.append({
            "type": "product",
            "file": pf,
            "label": "產品正面圖"
        })
    
    # 加 slider_no0xxx.jpg（滑面圖/細節圖）
    slider_files = sorted([
        f for f in os.listdir(num)
        if f.startswith("slider_no") and f.endswith(('.jpg', '.png'))
    ])
    for sf in slider_files:
        gallery_items.append({
            "type": "slider",
            "file": sf,
            "label": "產品細節圖"
        })
    
    # 加 use_place0xxx.jpg（使用場景圖）
    use_place_files = sorted([
        f for f in os.listdir(num)
        if f.startswith("use_place") and f.endswith(('.jpg', '.png'))
    ])
    for uf in use_place_files:
        gallery_items.append({
            "type": "use_place",
            "file": uf,
            "label": "使用場景圖"
        })
    
    # 用 product0xxx.jpg 作為主圖
    if product_files:
        main_img = product_files[0]
    else:
        main_img = slider_files[0] if slider_files else None
    
    # 生成標籤 HTML
    tags_html = ""
    for tag in info["tags"]:
        tags_html += f'            <span class="product-tag">{tag}</span>\n'
    
    # 生成多圖 HTML
    gallery_html = ""
    for item in gallery_items:
        gallery_html += f'''            <div class="gallery-item">
                <img src="{item['file']}" alt="{item['label']}">
            </div>
            <div class="gallery-label">{item['label']}</div>
'''
    
    html = base_template.replace("{num}", num)
    html = html.replace("{name}", info["name"])
    html = html.replace("{cat}", info["cat"])
    html = html.replace("{desc}", info["desc"])
    html = html.replace("{tags}", tags_html)
    html = html.replace("{gallery}", gallery_html)
    html = html.replace("{main_img}", main_img)
    
    # 把 {{ 換成 {（CSS 需要）
    html = html.replace("{{", "{").replace("}}", "}")
    
    os.makedirs(num, exist_ok=True)
    with open(f"{num}/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {num}: {info['name']} ({info['cat']}) - {len(product_files)} product + {len(slider_files)} slider + {len(use_place_files)} use_place = {len(gallery_items)} total images")

print(f"\n全部完成！共 {len(product_dirs)} 個產品頁")
