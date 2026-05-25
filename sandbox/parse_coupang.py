import re
import json

with open(r"C:\Users\leecmin\Desktop\coupang_source.txt.txt", "r", encoding="utf-8") as f:
    html = f.read()

print(f"HTML size: {len(html):,} chars")
print()

# Try to find JSON data blocks with product info
# Look for vendorItemId patterns with surrounding context
pattern = r'"vendorItemId"\s*:\s*"?(\d+)"?'
vendor_ids = re.findall(pattern, html)
print(f"Found {len(vendor_ids)} vendorItemId entries")

# Look for product name patterns
name_pattern = r'"name"\s*:\s*"([^"]+)"'
names = re.findall(name_pattern, html)
print(f"Found {len(names)} name entries")

# Look for salePrice
price_pattern = r'"salePrice"\s*:\s*"?(\d+)"?'
prices = re.findall(price_pattern, html)
print(f"Found {len(prices)} salePrice entries")

# Look for larger JSON structures - try to find script tags with JSON
script_pattern = r'<script[^>]*>(\{[^<]{500,})</script>'
scripts = re.findall(script_pattern, html)
print(f"\nFound {len(scripts)} large script blocks")

# Try to find product data structure
product_pattern = r'\{[^{}]*"vendorItemId"[^{}]*"name"[^{}]*\}'
products_raw = re.findall(product_pattern, html[:200000])
print(f"Found {len(products_raw)} product-like objects (first half)")

# Alternative: look for the data in a structured way
# Find all JSON-like blocks that contain vendorItemId
print("\n=== Extracting product data ===\n")

# Try parsing the large line (line 2 and 6 contain the data)
lines = html.split('\n')
print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines):
    if 'vendorItemId' in line:
        print(f"\nLine {i+1} length: {len(line):,} chars")
        # Find all product entries in this line
        # Look for patterns like {"vendorItemId":"xxx","itemId":"xxx","productId":"xxx",...}
        item_pattern = r'"vendorItemId"\s*:\s*"(\d+)"[^}]*?"name"\s*:\s*"([^"]*)"'
        items = re.findall(item_pattern, line)
        if items:
            print(f"  Found {len(items)} items with vendorItemId+name")
            for j, (vid, name) in enumerate(items[:5]):
                print(f"    [{j+1}] vendorItemId={vid}, name={name}")

        # Try another pattern
        item_pattern2 = r'"itemId"\s*:\s*"(\d+)"'
        item_ids = re.findall(item_pattern2, line)
        print(f"  itemIds found: {len(item_ids)}")

        # Extract a sample chunk around vendorItemId
        idx = line.find('vendorItemId')
        if idx > 0:
            sample = line[max(0,idx-100):idx+500]
            print(f"\n  Sample context around first vendorItemId:")
            print(f"  {sample[:600]}")
        break  # Just check first line with data
