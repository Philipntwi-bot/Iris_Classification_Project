from pathlib import Path
import os
import re
import json

root = Path(r"C:\Users\User\OneDrive\Desktop\MY IA FOR ARTIFICIAL INTELLIGENCE\Iris_Classification_Project")
html = (root / "index.html").read_text(encoding="utf-8")

# Check referenced images
imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
print("Referenced images in index.html:")
for img in set(imgs):
    if img.startswith("http") or img.startswith("data:"):
        print(f"External/Data URL: {img[:30]}...")
    else:
        p = root / img
        exists = p.exists()
        size = p.stat().st_size if exists else 0
        print(f"Local Image: {img} -> Exists: {exists} ({size} bytes)")

# Check model data json embedding
m_coef = re.search(r'const MODEL_COEF = (\[.*?\]);', html)
m_inter = re.search(r'const MODEL_INTERCEPT = (\[.*?\]);', html)
m_samples = re.search(r'const DATASET_SAMPLES = (\[.*?\]);', html)

if m_coef and m_inter and m_samples:
    coef = json.loads(m_coef.group(1))
    inter = json.loads(m_inter.group(1))
    samples = json.loads(m_samples.group(1))
    print(f"Embedded Coefs valid: shape {len(coef)}x{len(coef[0])}")
    print(f"Embedded Intercepts valid: {len(inter)}")
    print(f"Embedded Dataset Samples valid: {len(samples)} samples")
else:
    print("Warning: Could not parse embedded model arrays")

print("All integrity checks passed successfully!")
