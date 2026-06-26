import os
from PIL import Image

base = r"F:\工作區\昇銓手機版\products\紅螞蟻產品目錄"

for i in range(1, 36):
    dir_path = os.path.join(base, str(i))
    if not os.path.isdir(dir_path):
        print(f"分類 {i}: 不存在")
        continue
    
    files = sorted(os.listdir(dir_path))
    jpgs = [f for f in files if f.lower().endswith(('.jpg','.jpeg','.png','.webp'))]
    
    sizes = []
    for f in jpgs:
        try:
            img = Image.open(os.path.join(dir_path, f))
            sizes.append(f"{f}: {img.size[0]}x{img.size[1]}")
        except:
            sizes.append(f"{f}: ERROR")
    
    print(f"\n=== 分類 {i} ({len(jpgs)} 張圖片) ===")
    for s in sizes:
        print(f"  {s}")
