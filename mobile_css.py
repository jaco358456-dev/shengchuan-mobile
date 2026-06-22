#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""給所有 HTML 檔案批量加上手機版響應式 CSS"""

import os
import re
from pathlib import Path

# 手機版 CSS（所有頁面通用）
MOBILE_CSS = """
        /* =========================================
           手機版響應式
           ========================================= */
        @media (max-width: 768px) {
            /* 導覽列 */
            header { padding: 15px 20px !important; }
            .hamburger { display: flex !important; }
            .nav-links { display: none !important; }
            
            /* Hero / 首圖 */
            .hero { flex-direction: column !important; padding: 100px 20px 40px !important; min-height: auto !important; }
            .hero-text { flex: 0 0 auto !important; width: 100% !important; padding-right: 0 !important; text-align: center !important; margin-bottom: 40px !important; }
            .hero-text h1 { font-size: 2rem !important; }
            .hero-text p { font-size: 0.9rem !important; margin-bottom: 24px !important; }
            .hero-media { flex: 0 0 auto !important; width: 100% !important; height: 50vh !important; }
            .hero-poster-card { width: 200px !important; bottom: -30px !important; right: 0 !important; left: 0 !important; margin: 0 auto !important; }
            
            /* 影片區 */
            .video-section { padding: 60px 20px !important; }
            .video-container { grid-template-columns: 1fr !important; gap: 40px !important; }
            .video-frame { aspect-ratio: 16 / 9 !important; }
            .video-text { text-align: center !important; }
            .video-text h2 { font-size: 1.8rem !important; }
            .video-text p { font-size: 0.95rem !important; }
            
            /* AI / 大使 / 品牌區 */
            .ai-section, .ambassador-section, .campaign-section { flex-direction: column !important; gap: 30px !important; padding: 80px 20px !important; }
            .ai-text, .ambassador-text, .campaign-text { flex: 0 0 auto !important; width: 100% !important; padding-right: 0 !important; text-align: center !important; }
            .ai-text h2, .ambassador-text h2, .campaign-text h2 { font-size: 2rem !important; letter-spacing: 3px !important; }
            .ai-text .tagline, .ambassador-text .role { font-size: 0.95rem !important; }
            .ai-text p, .ambassador-text p, .campaign-text p { font-size: 0.95rem !important; }
            .ai-image, .ambassador-image, .campaign-image { flex: 0 0 auto !important; width: 100% !important; height: 350px !important; }
            
            /* 產品區 */
            .products-grid { grid-template-columns: 1fr !important; }
            .products-grid .product-card { margin-bottom: 20px !important; }
            
            /* 聯絡頁 */
            .contact-grid { grid-template-columns: 1fr !important; }
            .contact-card, .contact-form { padding: 30px !important; }
            .contact-item { flex-direction: column !important; gap: 4px !important; }
            .contact-label { width: auto !important; }
            
            /* 經銷商 */
            .dealer-grid { grid-template-columns: 1fr !important; }
            
            /* 頁尾 */
            footer { padding: 40px 20px !important; flex-direction: column !important; gap: 20px !important; text-align: center !important; }
            .footer-links a { margin: 0 10px !important; }
            .designer-footer { padding: 30px 20px !important; font-size: 0.8rem !important; }
        }
"""

def add_mobile_css(filepath):
    """在 HTML 檔案的 </style> 前插入手機版 CSS"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 檢查是否已經有手機版 media query
        if '@media (max-width: 768px)' in content:
            return False
        
        # 在 </style> 前面插入
        if '</style>' in content:
            new_content = content.replace('</style>', MOBILE_CSS + '\n        </style>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except Exception as e:
        print(f"  失敗: {filepath} - {e}")
    
    return False

def process_all_files(base_dir):
    """處理所有 HTML 檔案"""
    base = Path(base_dir)
    count = 0
    
    # 遍歷所有目錄和子目錄
    for html_file in base.rglob('*.html'):
        result = add_mobile_css(str(html_file))
        if result:
            count += 1
            print(f"  ✅ {html_file.relative_to(base)}")
        else:
            print(f"  ⏭️  跳過: {html_file.relative_to(base)}")
    
    print(f"\n共處理 {count} 個檔案")

if __name__ == '__main__':
    print("處理 F:/備份/昇銓手機版/ 所有 HTML 檔案...")
    process_all_files(r"F:/備份/昇銓手機版")
    print("完成！")
