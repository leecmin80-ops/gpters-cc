import re
import json
import csv
import os

with open(r"C:\Users\leecmin\Desktop\coupang_source.txt.txt", "r", encoding="utf-8") as f:
    html = f.read()

# Find JSON-LD script block (Schema.org structured data)
# Pattern: <script type="application/ld+json">...</script>
jsonld_pattern = r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>'
jsonld_blocks = re.findall(jsonld_pattern, html, re.DOTALL)

if not jsonld_blocks:
    # Try finding the ListItem pattern directly
    jsonld_pattern2 = r'\[(\{"@type":"ListItem".*?)\]'
    jsonld_blocks = re.findall(jsonld_pattern2, html, re.DOTALL)

# Also try to find the JSON structure with ListItem directly
list_pattern = r'(\[\s*\{"@type"\s*:\s*"ListItem".*?\}\s*\])'
list_matches = re.findall(list_pattern, html, re.DOTALL)

print(f"Found {len(jsonld_blocks)} JSON-LD blocks")
print(f"Found {len(list_matches)} ListItem arrays")

products = []

# Parse from the line that contains vendorItemId
lines = html.split('\n')
for line in lines:
    if 'vendorItemId' in line and '@type' in line:
        # Find the JSON-LD array in this line
        # Look for the array start
        start_idx = line.find('[{"@type":"ListItem"')
        if start_idx == -1:
            start_idx = line.find('[{"@type": "ListItem"')
        if start_idx == -1:
            # Try to find it differently
            start_idx = line.find('"@type":"ItemList"')
            if start_idx != -1:
                # Find the itemListElement array
                elem_idx = line.find('"itemListElement"', start_idx)
                if elem_idx != -1:
                    arr_start = line.find('[', elem_idx)
                    if arr_start != -1:
                        start_idx = arr_start

        if start_idx >= 0:
            # Find the matching closing bracket
            depth = 0
            end_idx = start_idx
            for i in range(start_idx, min(start_idx + 50000, len(line))):
                if line[i] == '[':
                    depth += 1
                elif line[i] == ']':
                    depth -= 1
                    if depth == 0:
                        end_idx = i + 1
                        break

            json_str = line[start_idx:end_idx]
            try:
                data = json.loads(json_str)
                if isinstance(data, list):
                    for item in data:
                        if item.get('@type') == 'ListItem':
                            product = item.get('item', {})
                            url = product.get('url', '')
                            # Extract IDs from URL
                            item_id_match = re.search(r'itemId=(\d+)', url)
                            vendor_id_match = re.search(r'vendorItemId=(\d+)', url)
                            product_id_match = re.search(r'/products/(\d+)', url)

                            products.append({
                                'rank': item.get('position', ''),
                                'name': product.get('name', ''),
                                'price': product.get('offers', {}).get('price', ''),
                                'currency': product.get('offers', {}).get('priceCurrency', 'KRW'),
                                'rating': product.get('aggregateRating', {}).get('ratingValue', ''),
                                'review_count': product.get('aggregateRating', {}).get('reviewCount', ''),
                                'image': product.get('image', [''])[0] if product.get('image') else '',
                                'url': url,
                                'product_id': product_id_match.group(1) if product_id_match else '',
                                'item_id': item_id_match.group(1) if item_id_match else '',
                                'vendor_item_id': vendor_id_match.group(1) if vendor_id_match else '',
                            })
            except json.JSONDecodeError as e:
                print(f"JSON parse error: {e}")
                # Try a regex fallback
                pass

# If JSON parse failed, try regex extraction
if not products:
    print("\nTrying regex extraction...")
    item_pattern = r'"position"\s*:\s*(\d+).*?"name"\s*:\s*"([^"]*)".*?"price"\s*:\s*(\d+).*?"reviewCount"\s*:\s*(\d+).*?/products/(\d+)\?itemId=(\d+)&vendorItemId=(\d+)'
    matches = re.findall(item_pattern, html)
    for m in matches:
        products.append({
            'rank': m[0],
            'name': m[1],
            'price': m[2],
            'currency': 'KRW',
            'rating': '',
            'review_count': m[3],
            'image': '',
            'url': f'https://www.coupang.com/vp/products/{m[4]}?itemId={m[5]}&vendorItemId={m[6]}',
            'product_id': m[4],
            'item_id': m[5],
            'vendor_item_id': m[6],
        })

print(f"\n{'='*60}")
print(f"Total products extracted: {len(products)}")
print(f"{'='*60}\n")

if products:
    # Print summary
    for p in products[:10]:
        print(f"#{p['rank']} | {p['name'][:40]} | {int(p['price']):,}원 | ★{p['rating']} ({p['review_count']}리뷰)")
        print(f"     URL: {p['url'][:80]}")
        print()

    if len(products) > 10:
        print(f"... and {len(products) - 10} more products")

    # Save to CSV
    output_path = r"C:\Users\leecmin\Desktop\coupang_products.csv"
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['rank', 'name', 'price', 'currency', 'rating', 'review_count', 'url', 'product_id', 'item_id', 'vendor_item_id', 'image'])
        writer.writeheader()
        writer.writerows(products)
    print(f"\nCSV saved: {output_path}")

    # Also save as JSON
    json_path = r"C:\Users\leecmin\Desktop\coupang_products.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print(f"JSON saved: {json_path}")
else:
    print("No products found. Showing raw data samples...")
    for line in lines:
        if 'vendorItemId' in line:
            print(f"\nLine sample (first 2000 chars):")
            print(line[:2000])
            break
