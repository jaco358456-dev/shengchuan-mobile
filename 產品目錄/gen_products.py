# -*- coding: utf-8 -*-
import os

products = [
    {"id":1, "name":"大理石紋 A", "cat":"stone", "catName":"石材系列", "desc":"天然大理紋理，展現石材原始之美", "path":"1", "thumb":"1/product0832.jpg"},
    {"id":2, "name":"石灰岩 B", "cat":"stone", "catName":"石材系列", "desc":"質樸質感，營造簡約自然氛圍", "path":"2", "thumb":"2/product0720.jpg"},
    {"id":3, "name":"花崗岩 C", "cat":"stone", "catName":"石材系列", "desc":"堅硬耐用，適合高使用頻率空間", "path":"3", "thumb":"3/product0685.jpg"},
    {"id":4, "name":"板岩 D", "cat":"stone", "catName":"石材系列", "desc":"層疊紋理，展現自然粗獷之美", "path":"4", "thumb":"4/product0788.jpg"},
    {"id":5, "name":"橡木紋 E", "cat":"wood", "catName":"木紋系列", "desc":"溫潤木紋色調，營造溫馨居家氛圍", "path":"5", "thumb":"5/product0833.jpg"},
    {"id":6, "name":"胡桃木紋 F", "cat":"wood", "catName":"木紋系列", "desc":"深沉木紋色調，適合現代風格空間", "path":"6", "thumb":"6/product0727.jpg"},
    {"id":7, "name":"松木紋 G", "cat":"wood", "catName":"木紋系列", "desc":"明亮木紋色調，營造輕盈通透感", "path":"7", "thumb":"7/product0847.jpg"},
    {"id":8, "name":"柚木紋 H", "cat":"wood", "catName":"木紋系列", "desc":"高雅木紋色調，展現品味格調", "path":"8", "thumb":"8/product0647.jpg"},
    {"id":9, "name":"純白 I", "cat":"minimal", "catName":"現代極簡", "desc":"純淨白色調，打造明亮簡約空間", "path":"9", "thumb":"9/product0688.jpg"},
    {"id":10, "name":"水泥灰 J", "cat":"minimal", "catName":"現代極簡", "desc":"工業風水泥紋理，展現時髦態度", "path":"10", "thumb":"10/product0649.jpg"},
    {"id":11, "name":"珍珠灰 K", "cat":"minimal", "catName":"現代極簡", "desc":"柔和灰色調，營造寧靜氛圍", "path":"11", "thumb":"11/product0772.jpg"},
    {"id":12, "name":"星空黑 L", "cat":"minimal", "catName":"現代極簡", "desc":"深邃黑色調，展現沉穩氣質", "path":"12", "thumb":"12/product0676.jpg"},
    {"id":13, "name":"大理石拼花 M", "cat":"design", "catName":"設計款系列", "desc":"復古拼花圖案，展現藝術氣息", "path":"13", "thumb":"13/product0736.jpg"},
    {"id":14, "name":"幾何拼接 N", "cat":"design", "catName":"設計款系列", "desc":"現代幾何圖案，營造視覺層次", "path":"14", "thumb":"14/product0828.jpg"},
    {"id":15, "name":"抽象藝術 O", "cat":"design", "catName":"設計款系列", "desc":"自由抽象圖案，展現個性風格", "path":"15", "thumb":"15/product0694.jpg"},
    {"id":16, "name":"自然拼貼 P", "cat":"design", "catName":"設計款系列", "desc":"自然元素拼貼，呈現原始美感", "path":"16", "thumb":"16/product0746.jpg"},
    {"id":17, "name":"款式 Q", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"17", "thumb":"17/product0666.jpg"},
    {"id":18, "name":"款式 R", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"18", "thumb":"18/product0748.jpg"},
    {"id":19, "name":"款式 S", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path": "19", "thumb":"19/product0831.jpg"},
    {"id":20, "name":"款式 T", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"20", "thumb":"20/product0512.jpg"},
    {"id":21, "name":"款式 U", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"21", "thumb":"21/product0754.jpg"},
    {"id":22, "name":"款式 V", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"22", "thumb":"22/product0704.jpg"},
    {"id":23, "name":"款式 W", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"23", "thumb":"23/product0709.jpg"},
    {"id":24, "name":"款式 X", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"24", "thumb":"24/product0638.jpg"},
    {"id":25, "name":"款式 Y", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"25", "thumb":"25/product0738.jpg"},
    {"id":26, "name":"款式 Z", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"26", "thumb":"26/product0641.jpg"},
    {"id":27, "name":"款式 AA", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"27", "thumb":"27/product0716.jpg"},
    {"id":28, "name":"款式 AB", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"28", "thumb":"28/product0830.jpg"},
    {"id":29, "name":"款式 AC", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"29", "thumb":"29/product0826.jpg"},
    {"id":30, "name":"款式 AD", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"30", "thumb":"30/product0841.jpg"},
    {"id":31, "name":"款式 AE", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"31", "thumb":"31/product0851.jpg"},
    {"id":32, "name":"款式 AF", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"32", "thumb":"32/product0858.jpg"},
    {"id":33, "name":"款式 AG", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"33", "thumb":"33/product0855.jpg"},
    {"id":34, "name":"款式 AH", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"34", "thumb":"34/product0860.jpg"},
    {"id":35, "name":"款式 AI", "cat":"stone", "catName":"石材系列", "desc":"精選石材款式", "path":"35", "thumb":"35/product0871.jpg"}
]

for p in products:
    filepath = f"F:\\\\工作區\\\\昇銓手機版\\\\產品目錄\\\\{p['path']}\\\\index.html"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{catName} - {name} | 紅螞蟻磁磚</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #F8F6F2;
            --text-primary: #1A1A1A;
            --text-secondary: #666666;
            --brand-red: #E63946;
            --border-subtle: rgba(0,0,0,0.06);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        img {{ width: 100%; height: auto; display: block; }}
        body {{
            font-family: 'Noto Sans TC', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            padding-top: 50px;
            padding-bottom: 80px;
        }}
        a {{ text-decoration: none; color: inherit; }}
        .mobile-header {{
            position: fixed; top: 0; left: 0; right: 0;
            height: 50px; background: rgba(248,246,242,0.95);
            backdrop-filter: blur(20px);
            display: flex; justify-content: space-between; align-items: center;
            padding: 0 12px; z-index: 1000;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .header-logo {{ height: 10px; width: auto; cursor: pointer; }}
        .hamburger {{ display: flex; flex-direction: column; gap: 4px; cursor: pointer; padding: 5px; }}
        .hamburger span {{ width: 22px; height: 2px; background: var(--text-primary); border-radius: 2px; }}
        .hamburger.active span:nth-child(1) {{ transform: rotate(45deg) translate(5px, 5px); }}
        .hamburger.active span:nth-child(2) {{ opacity: 0; }}
        .hamburger.active span:nth-child(3) {{ transform: rotate(-45deg) translate(6px, -6px); }}
        .header-contact {{
            font-size: 0.65rem; letter-spacing: 1px; color: var(--brand-red); font-weight: 500;
            padding: 6px 12px; border: 1px solid var(--brand-red); border-radius: 20px;
        }}
        .nav-overlay {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: var(--bg-primary); z-index: 999;
            transform: translateY(-100%); transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .nav-overlay.open {{ transform: translateY(0); }}
        .nav-overlay-content {{ padding: 70px 24px 40px; }}
        .nav-overlay-links a {{ display: block; padding: 16px 0; border-bottom: 1px solid rgba(0,0,0,0.06); }}
        .product-detail {{ max-width: 390px; margin: 0 auto; }}
        .product-gallery {{ position: relative; width: 100%; }}
        .product-gallery img {{ width: 100%; height: auto; display: block; }}
        .product-info {{ padding: 20px; }}
        .product-cat {{ font-size: 0.7rem; color: var(--text-secondary); letter-spacing: 1px; margin-bottom: 8px; }}
        .product-name {{ font-size: 1.4rem; font-weight: 700; margin-bottom: 12px; }}
        .product-desc {{ font-size: 0.9rem; color: var(--text-secondary); line-height: 1.8; margin-bottom: 20px; }}
        .product-features {{
            background: var(--bg-primary); border-radius: 12px; padding: 16px; margin-bottom: 20px;
        }}
        .product-features h3 {{ font-size: 0.8rem; margin-bottom: 12px; color: var(--text-secondary); }}
        .feature-item {{
            display: flex; align-items: center; gap: 8px; padding: 8px 0;
            border-bottom: 1px solid rgba(0,0,0,0.04); font-size: 0.85rem;
        }}
        .feature-item:last-child {{ border-bottom: none; }}
        .feature-icon {{ color: var(--brand-red); }}
        .back-link {{
            display: block; text-align: center; padding: 14px;
            background: var(--brand-red); color: #fff; border-radius: 12px;
            font-weight: 500; margin-top: 20px;
        }}
        .footer-bar {{
            padding: 24px 20px; border-top: 1px solid var(--border-subtle);
            display: flex; justify-content: space-between; align-items: center; background: var(--bg-primary);
        }}
        .footer-logo {{ height: 24px; width: auto; opacity: 0.4; }}
        .footer-icons {{ display: flex; gap: 12px; align-items: center; }}
        .footer-icons img {{ height: 24px; width: auto; opacity: 0.6; }}
        .designer-box {{
            padding: 24px 20px; background: #1A1A1A; color: #999;
            text-align: center; font-size: 0.75rem; line-height: 1.8;
        }}
        .designer-box a {{ color: #fff; text-decoration: underline; }}
        .bottom-nav {{
            position: fixed; bottom: 0; left: 0; right: 0;
            height: 70px; background: rgba(248,246,242,0.95);
            backdrop-filter: blur(20px);
            display: flex; justify-content: space-around; align-items: center;
            padding-bottom: env(safe-area-inset-bottom); z-index: 1000;
            border-top: 1px solid var(--border-subtle);
        }}
        .nav-tab {{
            display: flex; flex-direction: column; align-items: center; gap: 4px;
            font-size: 0.6rem; color: var(--text-secondary); padding: 6px 4px;
        }}
        .nav-tab.active {{ color: var(--brand-red); }}
        .nav-tab svg {{ width: 22px; height: 22px; stroke: currentColor; fill: none; stroke-width: 1.5; }}
    </style>
</head>
<body>
    <header class="mobile-header">
        <img src="../logos/logo.png" alt="紅螞蟻磁磚 Logo" class="header-logo" onclick="toggleNav()">
        <div class="hamburger" id="hamburger" onclick="toggleNav()">
            <span></span><span></span><span></span>
        </div>
        <a href="../聯絡我們/index.html" class="header-contact">聯絡我們</a>
    </header>
    <div class="nav-overlay" id="navOverlay">
        <div class="nav-overlay-content">
            <div class="nav-overlay-links">
                <a href="../index.html">首頁</a>
                <a href="../官方影片/index.html">官方影片</a>
                <a href="../產品目錄/index.html">產品目錄</a>
                <a href="../經銷商/index.html">全台經銷商</a>
                <a href="../聯絡我們/index.html">聯絡我們</a>
            </div>
        </div>
    </div>
    <div class="product-detail">
        <div class="product-gallery">
            <img src="{thumb}" alt="{name}">
        </div>
        <div class="product-info">
            <div class="product-cat">{catName}</div>
            <h1 class="product-name">{name}</h1>
            <div class="product-desc">{desc}</div>
            <div class="product-features">
                <h3>產品特色</h3>
                <div class="feature-item"><span class="feature-icon">◆</span><span>堅硬耐用，耐磨抗刮</span></div>
                <div class="feature-item"><span class="feature-icon">◆</span><span>防水防潮，適合各種空間</span></div>
                <div class="feature-item"><span class="feature-icon">◆</span><span>自然紋理，質感溫潤</span></div>
                <div class="feature-item"><span class="feature-icon">◆</span><span>易於清潔保養</span></div>
            </div>
            <a href="tel:0968527968" class="back-link">立即諮詢</a>
        </div>
        <div class="footer-bar">
            <img src="../logos/logo.png" alt="紅螞蟻磁磚 Logo" class="footer-logo">
            <div class="footer-icons">
                <img src="../logos/icon-fb.png" alt="Facebook">
                <img src="../logos/icon-ig.png" alt="Instagram">
                <img src="../logos/icon-yt.png" alt="YouTube">
            </div>
        </div>
        <div class="designer-box">
            <p>本網站由 <a href="https://www.tiktok.com/@zz489320" target="_blank">刷個存在感</a> 設計製作</p>
            <p>TikTok：@zz489320 ｜ 電話：0968 527 968</p>
        </div>
    </div>
    <nav class="bottom-nav">
        <a href="../index.html" class="nav-tab"><svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg><span>首頁</span></a>
        <a href="../產品目錄/index.html" class="nav-tab active"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg><span>產品</span></a>
        <a href="../官方影片/index.html" class="nav-tab"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg><span>影片</span></a>
        <a href="../經銷商/index.html" class="nav-tab"><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg><span>經銷商</span></a>
        <a href="../聯絡我們/index.html" class="nav-tab"><svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><span>聯絡</span></a>
    </nav>
    <script>function toggleNav(){{var o=document.getElementById('navOverlay');var h=document.getElementById('hamburger');o.classList.toggle('open');h.classList.toggle('active');}}</script>
</body>
</html>'''.format(**p))
    print(f"OK: {p['path']}/index.html - {p['name']}")
print("Done!")