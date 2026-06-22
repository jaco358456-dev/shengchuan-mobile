import os

files_to_fix = []
# 全系列產品
files_to_fix.append(r"F:\客戶委託專案\昇銓建材\website\全系列產品\AI圖形製作(3).html")
# 官方影片
files_to_fix.append(r"F:\客戶委託專案\昇銓建材\website\官方影片\index.html")
# 產品目錄首頁
files_to_fix.append(r"F:\客戶委託專案\昇銓建材\website\產品目錄\index.html")
# 35 個產品頁面
for i in range(1, 36):
    files_to_fix.append(f"F:\\客戶委託專案\\昇銓建材\\website\\產品目錄\\{i}\\{i}.html")

count = 0
for fp in files_to_fix:
    if not os.path.exists(fp):
        print(f"SKIP: {fp} not found")
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<a href="../第一頁(1).html#contacts">CONTACTS</a>' in content:
        content = content.replace('<a href="../第一頁(1).html#contacts">CONTACTS</a>', '<a href="../聯絡我們/index.html">聯絡我們</a>')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"FIXED: {os.path.basename(fp)}")
    else:
        print(f"SKIP: {os.path.basename(fp)} - no CONTACTS found")

print(f"\nDone. Fixed {count} files.")
