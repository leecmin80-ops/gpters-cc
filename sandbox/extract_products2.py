import re
import json
import csv

with open(r"C:\Users\leecmin\Desktop\coupang_source.txt.txt", "r", encoding="utf-8") as f:
    html = f.read()

products = []

# Find line with vendorItemId and extract JSON-LD
lines = html.split('\n')
for line in lines:
    if 'vendorItemId' not in line:
        continue

    # Find ItemList JSON-LD structure
    idx = line.find('"@type":"ItemList"')
    if idx == -1:
        idx = line.find('"@type": "ItemList"')
    if idx == -1:
        # Try to find the script tag containing the data
        script_start = line.rfind('<script', 0, line.find('vendorItemId'))
        script_end = line.find('</script>', line.find('vendorItemId'))
        if script_start != -1 and script_end != -1:
            json_candidate = line[script_start:script_end]
            # Extract just the JSON part
            json_start = json_candidate.find('>')
            if json_start != -1:
                json_str = json_candidate[json_start+1:]
                try:
                    data = json.loads(json_str)
                    print(f"Parsed JSON-LD, type: {data.get('@type', 'unknown')}")
                    print(f"Keys: {list(data.keys())[:10]}")
                    if 'itemListElement' in data:
                        elements = data['itemListElement']
                        print(f"Found {len(elements)} items in itemListElement")
                        for elem in elements:
                            item = elem.get('item', elem)
                            if isinstance(item, str):
                                # item is just a URL string
                                url = item
                                products.append({
                                    'rank': elem.get('position', ''),
                                    'name': '',
                                    'price': '',
                                    'url': url,
                                })
                            elif isinstance(item, dict):
                                url = item.get('url', '')
                                products.append({
                                    'rank': elem.get('position', ''),
                                    'name': item.get('name', ''),
                                    'price': item.get('offers', {}).get('price', '') if isinstance(item.get('offers'), dict) else '',
                                    'rating': item.get('aggregateRating', {}).get('ratingValue', '') if isinstance(item.get('aggregateRating'), dict) else '',
                                    'review_count': item.get('aggregateRating', {}).get('reviewCount', '') if isinstance(item.get('aggregateRating'), dict) else '',
                                    'url': url,
                                    'image': item.get('image', [''])[0] if isinstance(item.get('image'), list) else item.get('image', ''),
                                })
                except json.JSONDecodeError:
                    pass
        continue

    # Found ItemList, now find the containing script tag
    script_start = line.rfind('<script', 0, idx)
    script_end = line.find('</script>', idx)
    if script_start != -1 and script_end != -1:
        json_start = line.find('>', script_start) + 1
        json_str = line[json_start:script_end]
        try:
            data = json.loads(json_str)
            elements = data.get('itemListElement', [])
            print(f"Found ItemList with {len(elements)} items")
            for elem in elements:
                item = elem.get('item', elem)
                if isinstance(item, str):
                    products.append({'rank': elem.get('position', ''), 'name': '', 'price': '', 'url': item})
                elif isinstance(item, dict):
                    url = item.get('url', '')
                    products.append({
                        'rank': elem.get('position', ''),
                        'name': item.get('name', ''),
                        'price': item.get('offers', {}).get('price', '') if isinstance(item.get('offers'), dict) else '',
                        'rating': item.get('aggregateRating', {}).get('ratingValue', '') if isinstance(item.get('aggregateRating'), dict) else '',
                        'review_count': item.get('aggregateRating', {}).get('reviewCount', '') if isinstance(item.get('aggregateRating'), dict) else '',
                        'url': url,
                        'image': item.get('image', [''])[0] if isinstance(item.get('image'), list) else item.get('image', ''),
                    })
        except json.JSONDecodeError as e:
            print(f"Parse error: {e}")

# If still no products, use regex as fallback
if not products:
    print("\nUsing regex fallback...")
    # Pattern: "position":N ... "name":"..." ... "price":NNNN ... url with IDs
    pattern = r'"position"\s*:\s*(\d+)[^}]*?"@type"\s*:\s*"Product"[^}]*?"name"\s*:\s*"([^"]*)"'
    matches = re.findall(pattern, html)
    print(f"Regex found {len(matches)} position+name pairs")

    # Get all data with a broader pattern
    full_pattern = r'\{"@type":"ListItem","position":(\d+),"item":\{"@type":"Product","name":"([^"]*)","image":\["([^"]*)"\],"offers":\{"@type":"Offer","price":(\d+),"priceCurrency":"(\w+)"\},"aggregateRating":\{"@type":"AggregateRating","ratingValue":([\d.]+),"reviewCount":(\d+)\},"url":"([^"]*)"\}\}'
    full_matches = re.findall(full_pattern, html)
    print(f"Full regex found {len(full_matches)} complete product entries")

    for m in full_matches:
        url = m[7]
        product_id_match = re.search(r'/products/(\d+)', url)
        products.append({
            'rank': int(m[0]),
            'name': m[1],
            'image': m[2],
            'price': int(m[3]),
            'currency': m[4],
            'rating': float(m[5]),
            'review_count': int(m[6]),
            'url': url,
            'product_id': product_id_match.group(1) if product_id_match else '',
        })

# Extract IDs from URLs
for p in products:
    if p.get('url'):
        pid = re.search(r'/products/(\d+)', p['url'])
        iid = re.search(r'itemId=(\d+)', p['url'])
        vid = re.search(r'vendorItemId=(\d+)', p['url'])
        p['product_id'] = pid.group(1) if pid else p.get('product_id', '')
        p['item_id'] = iid.group(1) if iid else ''
        p['vendor_item_id'] = vid.group(1) if vid else ''

print(f"\n{'='*60}")
print(f"Total products extracted: {len(products)}")
print(f"{'='*60}\n")

if products:
    for p in products[:15]:
        name = p.get('name', '?')[:45]
        price = p.get('price', '?')
        rating = p.get('rating', '?')
        reviews = p.get('review_count', '?')
        rank = p.get('rank', '?')
        price_str = f"{int(price):,}원" if price and price != '?' else '?'
        print(f"#{rank:>2} | {name:<45} | {price_str:>10} | ★{rating} ({reviews}리뷰)")

    if len(products) > 15:
        print(f"\n... and {len(products) - 15} more products")

    # Save CSV
    output_path = r"C:\Users\leecmin\Desktop\coupang_products.csv"
    fieldnames = ['rank', 'name', 'price', 'currency', 'rating', 'review_count', 'url', 'product_id', 'item_id', 'vendor_item_id', 'image']
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(products)
    print(f"\nCSV saved: {output_path}")

    # Save JSON
    json_path = r"C:\Users\leecmin\Desktop\coupang_products.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print(f"JSON saved: {json_path}")
