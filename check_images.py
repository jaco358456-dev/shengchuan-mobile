from PIL import Image
import os

dirs = [
    "F:/工作區/昇銓手機版/hero",
    "F:/工作區/昇銓手機版/logos",
    "F:/工作區/昇銓手機版/昇銓建材/昇銓建材AI代理人",
    "F:/工作區/昇銓手機版/昇銓建材/昇銓建材圖檔製作素材區",
]

for d in dirs:
    print(f"\n{'='*60}")
    print(f"DIR: {d}")
    print(f"{'='*60}")
    if not os.path.exists(d):
        print("NOT FOUND")
        continue
    for f in sorted(os.listdir(d)):
        ext = os.path.splitext(f)[1].lower()
        if ext in ('.jpg','.jpeg','.png','.webp','.gif'):
            path = os.path.join(d, f)
            try:
                img = Image.open(path)
                print(f"  {f}: {img.size[0]}x{img.size[1]} mode={img.mode}")
            except Exception as e:
                print(f"  {f}: ERROR {e}")
        else:
            sz = os.path.getsize(path)
            print(f"  {f}: {sz/1024:.1f}KB (non-image)")

# Also check logo.PNG in root
logo_path = r"F:\工作區\昇銓手機版\logos\logo.PNG"
if os.path.exists(logo_path):
    img = Image.open(logo_path)
    print(f"\n  logo.PNG: {img.size[0]}x{img.size[1]} mode={img.mode}")
