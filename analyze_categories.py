import os, subprocess

base = r"F:\工作區\昇銓手機版\products\紅螞蟻產品目錄"

print("="*80)
print("紅螞蟻產品目錄結構分析")
print("="*80)

# 列出 1-35 每個分類的檔案
for i in range(1, 36):
    dir_path = os.path.join(base, str(i))
    if os.path.isdir(dir_path):
        files = os.listdir(dir_path)
        product_files = [f for f in files if f.startswith("product")]
        slider_files = [f for f in files if f.startswith("slider")]
        use_place_files = [f for f in files if f.startswith("use_place")]
        html_files = [f for f in files if f.endswith(".html")]
        
        print(f"\n分類 {i}: {len(product_files)} products, {len(slider_files)} sliders, {len(use_place_files)} use_place")
        if product_files:
            print(f"  product: {', '.join(product_files)}")
        if slider_files:
            print(f"  slider: {', '.join(slider_files)}")
        if use_place_files:
            print(f"  use_place: {', '.join(use_place_files)}")
    else:
        print(f"分類 {i}: 不存在")

# 列出根目錄
print("\n" + "="*80)
print("根目錄檔案")
print("="*80)
for f in sorted(os.listdir(base)):
    fpath = os.path.join(base, f)
    if os.path.isdir(fpath):
        print(f"[DIR] {f}")
    elif os.path.isfile(fpath):
        sz = os.path.getsize(fpath)
        print(f"  {f} ({sz/1024:.1f}KB)")
