import re
import json
import csv

# Try different encodings
for enc in ['utf-8', 'cp949', 'euc-kr', 'utf-8-sig']:
    try:
        with open(r"C:\Users\leecmin\Desktop\coupang_source.txt.txt", "r", encoding=enc) as f:
            html = f.read()
        # Test if Korean text is readable
        if '쿠팡' in html or '상품' in html or '리뷰' in html or '원' in html:
            print(f"Encoding: {enc} (Korean text OK)")
            break
        elif 'coupang' in html.lower():
            print(f"Encoding: {enc} (no Korean detected, but file readable)")
    except (UnicodeDecodeError, LookupError):
        continue

products = []

# Find line with vendorItemId
lines = html.split('\n')
for line in lines:
    if 'vendorItemId' not in line or '@type' not in line:
        continue

    # Use regex to extract complete product entries
    full_pattern = r'\{"@type":"ListItem","position":(\d+),"item":\{"@type":"Product","name":"([^"]*)","image":\["([^"]*)"\],"offers":\{"@type":"Offer","price":(\d+),"priceCurrency":"(\w+)"\},"aggregateRating":\{"@type":"AggregateRating","ratingValue":([\d.]+),"reviewCount":(\d+)\},"url":"([^"]*)"\}\}'
    matches = re.findall(full_pattern, line)

    for m in matches:
        url = m[7]
        pid = re.search(r'/products/(\d+)', url)
        iid = re.search(r'itemId=(\d+)', url)
        vid = re.search(r'vendorItemId=(\d+)', url)
        products.append({
            'rank': int(m[0]),
            'name': m[1],
            'image': m[2],
            'price': int(m[3]),
            'currency': m[4],
            'rating': float(m[5]),
            'review_count': int(m[6]),
            'url': url,
            'product_id': pid.group(1) if pid else '',
            'item_id': iid.group(1) if iid else '',
            'vendor_item_id': vid.group(1) if vid else '',
        })
    break

print(f"\n{'='*70}")
print(f"  쿠팡 카테고리 순위 상품 데이터 ({len(products)}개 추출)")
print(f"{'='*70}\n")

if products:
    print(f"{'순위':>4} | {'상품명':<50} | {'가격':>10} | {'별점':>4} | {'리뷰수':>8}")
    print("-" * 90)
    for p in products:
        name = p['name'][:48]
        print(f"  {p['rank']:>2} | {name:<50} | {p['price']:>8,}원 | {p['rating']:>4} | {p['review_count']:>6,}개")

    # Save CSV (UTF-8 BOM for Excel compatibility)
    output_path = r"C:\Users\leecmin\Desktop\coupang_products.csv"
    fieldnames = ['rank', 'name', 'price', 'currency', 'rating', 'review_count', 'url', 'product_id', 'item_id', 'vendor_item_id', 'image']
    with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

    # Save JSON
    json_path = r"C:\Users\leecmin\Desktop\coupang_products.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*70}")
    print(f"  파일 저장 완료!")
    print(f"  - CSV: {output_path}")
    print(f"  - JSON: {json_path}")
    print(f"{'='*70}")
    print(f"\n  CSV 파일을 엑셀에서 열면 상품 데이터를 볼 수 있습니다.")
