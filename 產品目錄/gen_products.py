import os

products = {
    1: {'sku': '0832', 'name': '產品 0832', 'product_imgs': ['product0832.jpg'], 'slider_imgs': ['slider_no0058.jpg', 'slider_no0189.jpg'], 'use_imgs': []},
    2: {'sku': '0720', 'name': '產品 0720', 'product_imgs': ['product0720.jpg', 'product0722.jpg', 'product0723.jpg', 'product0724.jpg', 'product0820.jpg', 'product0821.jpg', 'product0868.jpg', 'product0870.jpg'], 'slider_imgs': ['slider_no0047.jpg', 'slider_no0049.jpg', 'slider_no0051.jpg', 'slider_no0163.jpg'], 'use_imgs': ['use_place0082.jpg']},
    3: {'sku': '0685', 'name': '產品 0685', 'product_imgs': ['product0685.jpg', 'product0813.jpg', 'product0814.jpg', 'product0815.jpg'], 'slider_imgs': ['slider_no0023.jpg', 'slider_no0024.jpg', 'slider_no0066.jpg'], 'use_imgs': []},
    4: {'sku': '0788', 'name': '產品 0788', 'product_imgs': ['product0788.jpg', 'product0842.jpg', 'product0843.jpg', 'product0844.jpg'], 'slider_imgs': ['slider_no0164.jpg', 'slider_no0166.jpg'], 'use_imgs': ['use_place0059.jpg', 'use_place0060.jpg', 'use_place0061.jpg', 'use_place0062.jpg']},
    5: {'sku': '0833', 'name': '產品 0833', 'product_imgs': ['product0833.jpg', 'product0834.jpg', 'product0835.jpg', 'product0836.jpg'], 'slider_imgs': ['slider_no0112.jpg', 'slider_no0113.jpg', 'slider_no0114.jpg', 'slider_no0115.jpg'], 'use_imgs': ['use_place0055.jpg', 'use_place0056.jpg', 'use_place0057.jpg', 'use_place0058.jpg']},
    6: {'sku': '0727', 'name': '產品 0727', 'product_imgs': ['product0727.jpg', 'product0731.jpg', 'product0811.jpg', 'product0812.jpg'], 'slider_imgs': ['slider_no0045.jpg', 'slider_no0046.jpg'], 'use_imgs': ['use_place0054.jpg']},
    7: {'sku': '0847', 'name': '產品 0847', 'product_imgs': ['product0847.jpg', 'product0848.jpg', 'product0849.jpg', 'product0850.jpg'], 'slider_imgs': ['slider_no0063.jpg', 'slider_no0118.jpg', 'slider_no0119.jpg'], 'use_imgs': []},
    8: {'sku': '0647', 'name': '產品 0647', 'product_imgs': ['product0647.jpg', 'product0648.jpg', 'product0878.jpg'], 'slider_imgs': ['slider_no0064.jpg'], 'use_imgs': ['use_place0046.jpg']},
    9: {'sku': '0688', 'name': '產品 0688', 'product_imgs': ['product0688.jpg', 'product0690.jpg', 'product0823.jpg', 'product0824.jpg'], 'slider_imgs': ['slider_no0065.jpg', 'slider_no0067.jpg', 'slider_no0197.jpg', 'slider_no0198.jpg'], 'use_imgs': []},
    10: {'sku': '0649', 'name': '產品 0649', 'product_imgs': ['product0649.jpg', 'product0650.jpg', 'product0651.jpg', 'product0652.jpg', 'product0653.jpg', 'product0654.jpg', 'product0655.jpg', 'product0657.jpg'], 'slider_imgs': ['slider_no0070.jpg', 'slider_no0071.jpg', 'slider_no0072.jpg', 'slider_no0073.jpg'], 'use_imgs': ['use_place0047.jpg', 'use_place0048.jpg', 'use_place0049.jpg']},
    11: {'sku': '0772', 'name': '產品 0772', 'product_imgs': ['product0772.jpg', 'product0773.jpg'], 'slider_imgs': ['slider_no0074.jpg', 'slider_no0187.jpg'], 'use_imgs': []},
    12: {'sku': '0676', 'name': '產品 0676', 'product_imgs': ['product0676.jpg', 'product0677.jpg', 'product0678.jpg', 'product0680.jpg', 'product0681.jpg', 'product0682.jpg', 'product0683.jpg', 'product0767.jpg'], 'slider_imgs': ['slider_no0131.jpg', 'slider_no0132.jpg', 'slider_no0133.jpg', 'slider_no0134.jpg', 'slider_no0135.jpg', 'slider_no0136.jpg', 'slider_no0137.jpg', 'slider_no0186.jpg'], 'use_imgs': []},
    13: {'sku': '0736', 'name': '產品 0736', 'product_imgs': ['product0736.jpg', 'product0737.jpg'], 'slider_imgs': ['slider_no0087.jpg', 'slider_no0089.jpg'], 'use_imgs': ['use_place0086.jpg']},
    14: {'sku': '0828', 'name': '產品 0828', 'product_imgs': ['product0828.jpg', 'product0829.jpg'], 'slider_imgs': ['slider_no0088.jpg'], 'use_imgs': []},
    15: {'sku': '0694', 'name': '產品 0694', 'product_imgs': ['product0694.jpg', 'product0809.jpg'], 'slider_imgs': ['slider_no0093.jpg', 'slider_no0094.jpg', 'slider_no0095.jpg'], 'use_imgs': []},
    16: {'sku': '0746', 'name': '產品 0746', 'product_imgs': ['product0746.jpg', 'product0747.jpg'], 'slider_imgs': ['slider_no0096.jpg', 'slider_no0097.jpg', 'slider_no0184.jpg'], 'use_imgs': []},
    17: {'sku': '0666', 'name': '產品 0666', 'product_imgs': ['product0666.jpg', 'product0668.jpg', 'product0769.jpg', 'product0770.jpg', 'product0771.jpg'], 'slider_imgs': ['slider_no0101.jpg', 'slider_no0102.jpg', 'slider_no0103.jpg'], 'use_imgs': []},
    18: {'sku': '0748', 'name': '產品 0748', 'product_imgs': ['product0748.jpg', 'product0750.jpg'], 'slider_imgs': ['slider_no0105.jpg', 'slider_no0106.jpg', 'slider_no0206.jpg', 'slider_no0207.jpg'], 'use_imgs': []},
    19: {'sku': '0831', 'name': '產品 0831', 'product_imgs': ['product0831.jpg'], 'slider_imgs': ['slider_no0107.jpg', 'slider_no0190.jpg'], 'use_imgs': ['use_place0085.jpg']},
    20: {'sku': '0512', 'name': '產品 0512', 'product_imgs': ['product0512.jpg', 'product0513.jpg', 'product0514.jpg', 'product0515.jpg', 'product0517.jpg', 'product0518.jpg', 'product0519.jpg', 'product0520.jpg', 'product0522.jpg', 'product0523.jpg', 'product0525.jpg', 'product0527.jpg'], 'slider_imgs': ['slider_no0116.jpg', 'slider_no0117.jpg'], 'use_imgs': []},
    21: {'sku': '0754', 'name': '產品 0754', 'product_imgs': ['product0754.jpg', 'product0755.jpg', 'product0756.jpg'], 'slider_imgs': ['slider_no0120.jpg', 'slider_no0121.jpg', 'slider_no0202.jpg', 'slider_no0203.jpg', 'slider_no0204.jpg'], 'use_imgs': []},
    22: {'sku': '0704', 'name': '產品 0704', 'product_imgs': ['product0704.jpg', 'product0705.jpg', 'product0819.jpg', 'product0877.jpg'], 'slider_imgs': ['slider_no0138.jpg', 'slider_no0139.jpg', 'slider_no0140.jpg', 'slider_no0181.jpg', 'slider_no0182.jpg'], 'use_imgs': []},
    23: {'sku': '0709', 'name': '產品 0709', 'product_imgs': ['product0709.jpg', 'product0711.jpg', 'product0807.jpg', 'product0838.jpg', 'product0839.jpg', 'product0840.jpg', 'product0861.jpg', 'product0864.jpg', 'product0865.jpg', 'product0866.jpg'], 'slider_imgs': ['slider_no0141.jpg', 'slider_no0142.jpg', 'slider_no0143.jpg', 'slider_no0167.jpg', 'slider_no0168.jpg', 'slider_no0177.jpg', 'slider_no0185.jpg', 'slider_no0205.jpg'], 'use_imgs': ['use_place0074.jpg', 'use_place0075.jpg']},
    24: {'sku': '0638', 'name': '產品 0638', 'product_imgs': ['product0638.jpg', 'product0768.jpg', 'product0801.jpg', 'product0802.jpg', 'product0803.jpg'], 'slider_imgs': ['slider_no0144.jpg', 'slider_no0145.jpg', 'slider_no0147.jpg', 'slider_no0151.jpg'], 'use_imgs': []},
    25: {'sku': '0738', 'name': '產品 0738', 'product_imgs': ['product0738.jpg', 'product0739.jpg'], 'slider_imgs': ['slider_no0148.jpg', 'slider_no0149.jpg', 'slider_no0150.jpg'], 'use_imgs': []},
    26: {'sku': '0641', 'name': '產品 0641', 'product_imgs': ['product0641.jpg', 'product0642.jpg', 'product0643.jpg', 'product0644.jpg'], 'slider_imgs': ['slider_no0152.jpg', 'slider_no0153.jpg', 'slider_no0154.jpg', 'slider_no0155.jpg', 'slider_no0188.jpg'], 'use_imgs': []},
    27: {'sku': '0716', 'name': '產品 0716', 'product_imgs': ['product0716.jpg', 'product0804.jpg', 'product0805.jpg'], 'slider_imgs': ['slider_no0157.jpg', 'slider_no0158.jpg', 'slider_no0159.jpg'], 'use_imgs': []},
    28: {'sku': '0830', 'name': '產品 0830', 'product_imgs': ['product0830.jpg'], 'slider_imgs': ['slider_no0160.jpg', 'slider_no0195.jpg'], 'use_imgs': []},
    29: {'sku': '0826', 'name': '產品 0826', 'product_imgs': ['product0826.jpg', 'product0827.jpg'], 'slider_imgs': ['slider_no0161.jpg'], 'use_imgs': []},
    30: {'sku': '0841', 'name': '產品 0841', 'product_imgs': ['product0841.jpg'], 'slider_imgs': ['slider_no0169.jpg'], 'use_imgs': []},
    31: {'sku': '0851', 'name': '產品 0851', 'product_imgs': ['product0851.jpg', 'product0852.jpg'], 'slider_imgs': ['slider_no0170.jpg', 'slider_no0171.jpg'], 'use_imgs': ['use_place0087.jpg']},
    32: {'sku': '0858', 'name': '產品 0858', 'product_imgs': ['product0858.jpg', 'product0859.jpg', 'product0862.jpg', 'product0863.jpg'], 'slider_imgs': ['slider_no0172.jpg', 'slider_no0173.jpg', 'slider_no0179.jpg'], 'use_imgs': []},
    33: {'sku': '0855', 'name': '產品 0855', 'product_imgs': ['product0855.jpg', 'product0856.jpg', 'product0857.jpg'], 'slider_imgs': ['slider_no0174.jpg', 'slider_no0175.jpg', 'slider_no0176.jpg'], 'use_imgs': []},
    34: {'sku': '0860', 'name': '產品 0860', 'product_imgs': ['product0860.jpg'], 'slider_imgs': ['slider_no0178.jpg', 'slider_no0196.jpg'], 'use_imgs': []},
    35: {'sku': '0871', 'name': '產品 0871', 'product_imgs': ['product0871.jpg', 'product0872.jpg', 'product0873.jpg', 'product0874.jpg', 'product0875.jpg', 'product0876.jpg'], 'slider_imgs': ['slider_no0180.jpg'], 'use_imgs': ['use_place0088.jpg', 'use_place0089.jpg', 'use_place0090.jpg', 'use_place0091.jpg', 'use_place0092.jpg', 'use_place0093.jpg']},
}

base_css = """
        :root {
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
        .product-page {
            padding: 140px 40px 80px;
            max-width: 1400px;
            margin: 0 auto;
        }
        .product-header {
            margin-bottom: 60px;
            text-align: center;
        }
        .product-header h1 {
            font-size: clamp(2rem, 3.5vw, 3rem);
            font-weight: 300;
            letter-spacing: 4px;
            margin-bottom: 10px;
        }
        .product-header .sku {
            font-size: 0.95rem;
            color: var(--text-sub);
            letter-spacing: 3px;
        }
        .image-section {
            margin-bottom: 60px;
        }
        .image-section h2 {
            font-size: 1.5rem;
            font-weight: 300;
            letter-spacing: 3px;
            margin-bottom: 25px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--brand-red);
            display: inline-block;
            color: var(--brand-red);
        }
        .image-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .image-grid img {
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .image-grid img:hover {
            transform: scale(1.02);
        }
        .back-link {
            display: inline-block;
            margin-top: 40px;
            padding: 12px 30px;
            border: 1px solid var(--text-main);
            border-radius: 30px;
            color: var(--text-main);
            font-size: 0.9rem;
            letter-spacing: 2px;
            transition: all 0.3s;
        }
        .back-link:hover {
            background: var(--text-main);
            color: #fff;
        }
        footer {
            padding: 60px 40px;
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fff;
        }
        .footer-links a { margin-left: 30px; font-size: 0.8rem; color: var(--text-sub); }
        @media (max-width: 768px) {
            .image-grid { grid-template-columns: 1fr; }
        }
"""

for pid, data in products.items():
    imgs_html = ""
    for img in data['product_imgs']:
        imgs_html += '<div><img src="' + img + '" alt="' + img + '"></div>\n'

    dynamic_sections = ""
    if data['slider_imgs']:
        slider_imgs = ""
        for img in data['slider_imgs']:
            slider_imgs += '<div><img src="' + img + '" alt="' + img + '"></div>\n'
        dynamic_sections += '<div class="image-section"><h2>展示圖</h2><div class="image-grid">\n' + slider_imgs + '</div></div>'

    if data['use_imgs']:
        use_imgs = ""
        for img in data['use_imgs']:
            use_imgs += '<div><img src="' + img + '" alt="' + img + '"></div>\n'
        dynamic_sections += '<div class="image-section"><h2>應用場景</h2><div class="image-grid">\n' + use_imgs + '</div></div>'

    html = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>紅螞蟻磁磚 | """ + data["name"] + """</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
""" + base_css + """
    </style>
</head>
<body>
    <header>
        <img src="../圖片區/logos/logo.png" alt="紅螞蟻磁磚 Logo" class="nav-logo">
        <nav class="nav-links">
            <a href="../第一頁(1).html">首頁</a>
            <a href="../官方影片/index.html">官方影片</a>
            <a href="../全系列產品/AI圖形製作(3).html">風格總覽</a>
            <a href="../產品目錄/index.html">產品目錄</a>
            <a href="../第一頁(1).html#ai-section">AI 虛擬代言人</a>
            <a href="../第一頁(1).html#ambassador">品牌大使</a>
            <a href="../第一頁(1).html#contacts">CONTACTS</a>
        </nav>
    </header>
    <div class="product-page">
        <div class="product-header">
            <h1>""" + data["name"] + """</h1>
            <div class="sku">SKU: """ + data["sku"] + """</div>
        </div>

        <div class="image-section">
            <h2>產品圖</h2>
            <div class="image-grid">
""" + imgs_html + """            </div>
        </div>

""" + dynamic_sections + """
        <a href="../產品目錄/index.html" class="back-link">← 返回產品目錄</a>
    </div>
    <footer>
        <img src="../圖片區/logos/logo.png" alt="紅螞蟻 Logo" style="height: 30px; opacity: 0.5;">
        <div class="footer-links">
            <a href="#">Facebook</a>
            <a href="#">Instagram</a>
            <a href="#">TikTok</a>
        </div>
    </footer>
</body>
</html>
"""

    os.makedirs("F:/客戶委託專案/昇銓建材/website/產品目錄/" + str(pid), exist_ok=True)
    with open("F:/客戶委託專案/昇銓建材/website/產品目錄/" + str(pid) + "/" + str(pid) + ".html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated: " + str(pid) + "/" + str(pid) + ".html for " + data["sku"])

print("\nDone! 35 product pages created.")
