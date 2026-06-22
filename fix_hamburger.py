#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""給所有子頁面加上漢堡選單"""

import os
import re
from pathlib import Path

# 漢堡選單 CSS
HAMBURGER_CSS = """
        /* 漢堡選單按鈕 */
        .hamburger {
            display: none;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
            z-index: 1100;
            padding: 5px;
        }
        .hamburger span {
            width: 25px;
            height: 2px;
            background: var(--text-main);
            transition: all 0.3s;
            border-radius: 2px;
        }
        .hamburger.active span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
        .hamburger.active span:nth-child(2) { opacity: 0; }
        .hamburger.active span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }
        
        /* 手機版導覽列覆蓋層 */
        .mobile-nav-overlay {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(248, 246, 242, 0.95);
            backdrop-filter: blur(30px);
            z-index: 1050;
            display: flex;
            flex-direction: column;
            transform: translateY(-100%);
            transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .mobile-nav-overlay.open {
            transform: translateY(0);
        }
        .mobile-nav-header {
            padding: 80px 30px 30px;
            width: 100%;
        }
        .mobile-nav-close {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 40px;
        }
        .mobile-nav-back {
            font-size: 1rem;
            color: var(--text-main);
            text-decoration: none;
            padding: 12px 24px;
            border: 1px solid var(--text-main);
            border-radius: 30px;
            font-weight: 500;
            letter-spacing: 2px;
            transition: all 0.3s ease;
        }
        .mobile-nav-back:hover {
            background: var(--text-main);
            color: #fff;
        }
        .mobile-nav-close-btn {
            font-size: 1.5rem;
            color: var(--text-main);
            cursor: pointer;
            padding: 10px;
            border: none;
            background: none;
            transition: color 0.3s;
        }
        .mobile-nav-close-btn:hover {
            color: var(--brand-red);
        }
        .mobile-nav-title {
            font-size: 0.75rem;
            letter-spacing: 4px;
            color: var(--text-sub);
            margin-bottom: 20px;
            text-transform: uppercase;
        }
        .mobile-nav-links {
            display: flex;
            flex-direction: column;
            gap: 0;
            width: 100%;
        }
        .mobile-nav-links a {
            display: block;
            font-size: 1.5rem;
            font-weight: 400;
            color: var(--text-main);
            padding: 22px 30px;
            letter-spacing: 3px;
            transition: all 0.3s ease;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }
        .mobile-nav-links a:hover {
            color: var(--brand-red);
            padding-left: 40px;
            background: rgba(230, 57, 70, 0.03);
        }
        .mobile-nav-links a:last-child {
            border-bottom: none;
        }
        .mobile-nav-footer {
            margin-top: auto;
            padding: 30px;
        }
        .mobile-nav-pdf-link {
            display: block;
            text-align: center;
            background: var(--brand-red);
            color: #fff;
            padding: 18px 40px;
            border-radius: 30px;
            font-size: 1.1rem;
            font-weight: 500;
            letter-spacing: 3px;
            transition: background 0.3s ease;
        }
        .mobile-nav-pdf-link:hover {
            background: #c12d38;
            transform: translateY(-2px);
        }
"""

# 手機版 CSS 中的 header 和 hamburger 規則
MOBILE_CSS_REPLACEMENT = """            /* 導覽列 */
            header { padding: 15px 20px; }
            .hamburger { display: flex; }
            .nav-links { display: none; }"""

# 漢堡選單 HTML
HAMBURGER_HTML = """        <div class="hamburger" id="hamburger" onclick="toggleMobileNav()">
            <span></span>
            <span></span>
            <span></span>
        </div>
"""

# 手機版選單 HTML
MOBILE_NAV_HTML = """        <!-- 手機版導覽列覆蓋層 -->
        <div class="mobile-nav-overlay" id="mobileNav">
            <div class="mobile-nav-header">
                <div class="mobile-nav-close">
                    <a href="第一頁(1).html" class="mobile-nav-back" onclick="toggleMobileNav()">← 回首頁</a>
                    <button class="mobile-nav-close-btn" onclick="toggleMobileNav()">✕</button>
                </div>
                <div class="mobile-nav-title">導航選單</div>
                <div class="mobile-nav-links">
                    <a href="第一頁(1).html" onclick="toggleMobileNav()">首頁</a>
                    <a href="官方影片/index.html" onclick="toggleMobileNav()">官方影片</a>
                    <a href="全系列產品/AI圖形製作(3).html" onclick="toggleMobileNav()">風格總覽</a>
                    <a href="產品目錄/index.html" onclick="toggleMobileNav()">產品目錄</a>
                    <a href="經銷商/index.html" onclick="toggleMobileNav()">全台經銷商</a>
                    <a href="第一頁(1).html#ai-section" onclick="toggleMobileNav()">AI 虛擬代言人</a>
                    <a href="第一頁(1).html#ambassador" onclick="toggleMobileNav()">品牌大使</a>
                    <a href="聯絡我們/index.html" onclick="toggleMobileNav()">聯絡我們</a>
                </div>
            </div>
            <div class="mobile-nav-footer">
                <a href="電子書目錄/電子書目錄.pdf" class="mobile-nav-pdf-link" onclick="toggleMobileNav()">電子書目錄</a>
            </div>
        </div>
"""

# JS 函式
MOBILE_NAV_JS = """
        <!-- 手機版導覽列 JavaScript -->
        <script>
            function toggleMobileNav() {
                var overlay = document.getElementById('mobileNav');
                var hamburger = document.getElementById('hamburger');
                overlay.classList.toggle('open');
                hamburger.classList.toggle('active');
            }
        </script>
"""


def process_file(filepath):
    """處理單一 HTML 檔案"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    base_path = filepath.parent
    
    # 1. 在 header 的 .nav-links 前面加入 hamburger 按鈕
    # 找到 <nav class="nav-links"> 前面插入
    if 'class="nav-links"' in content:
        if 'class="hamburger"' not in content:
            content = content.replace(
                '<nav class="nav-links">',
                HAMBURGER_HTML + '        <nav class="nav-links">'
            )
            modified = True
    
    # 2. 在 </style> 前面加入 hamburger CSS
    if '<style>' in content and 'class="hamburger"' in content:
        if '.hamburger {' not in content:
            content = content.replace(
                '        </style>',
                HAMBURGER_CSS + '        </style>'
            )
            modified = True
    
    # 3. 修改手機版 CSS 中的 header/hamburger/nav-links 規則
    if '@media (max-width: 768px)' in content:
        # 檢查是否已有簡化的規則
        if 'header { padding: 15px 20px' in content and '.hamburger { display: flex' in content:
            content = content.replace(
                '            /* 導覽列 */\n            header { padding: 15px 20px !important; }\n            .hamburger { display: flex !important; }\n            .nav-links { display: none !important; }',
                MOBILE_CSS_REPLACEMENT
            )
            modified = True
    
    # 4. 在 nav 閉合標籤後面加入 mobile-nav-overlay
    if '<nav class="nav-links">' in content and 'mobile-nav-overlay' not in content:
        # 找到 nav 的閉合標籤
        content = content.replace(
            '        </nav>\n    </header>',
            '        </nav>\n' + MOBILE_NAV_HTML + '\n    </header>'
        )
        modified = True
    
    # 5. 在 </header> 後面加入 JS
    if '</header>' in content and 'toggleMobileNav' not in content:
        content = content.replace(
            '</header>',
            '</header>\n' + MOBILE_NAV_JS
        )
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


# 主程式
base_dir = Path('F:/備份/昇銓手機版')
processed = 0

for html_file in base_dir.rglob('*.html'):
    # 跳過首頁
    if '第一頁(1).html' in str(html_file):
        continue
    
    print(f'處理: {html_file}')
    if process_file(html_file):
        print(f'  ✅ 已更新')
        processed += 1
    else:
        print(f'  ⏭️ 已跳過')

print(f'\n✅ 共處理 {processed} 個檔案')
