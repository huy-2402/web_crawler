import requests
from bs4 import BeautifulSoup
import json
import os

def crawl_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        soup = BeautifulSoup(response.text, 'html.parser')

        # Lấy tiêu đề (ví dụ thẻ <h1> hoặc <h2>)
        title_tag = soup.find(['h1', 'h2'])
        title = title_tag.get_text(strip=True) if title_tag else None

        # Lấy mô tả (ví dụ thẻ <p> đầu tiên)
        desc_tag = soup.find('p')
        description = desc_tag.get_text(strip=True) if desc_tag else None

        # Lấy tất cả link (href) trong trang
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return {
            'url': url,
            'title': title,
            'description': description,
            'links': links
        }
    except Exception as e:
        print(f"Lỗi khi crawl {url}: {e}")
        return None

def crawl_multiple_pages(urls):
    results = []
    for url in urls:
        print(f"Crawling {url} ...")
        data = crawl_page(url)
        if data:
            results.append(data)
    return results

def save_to_json(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    urls = [
        'https://example.com',
        'https://www.python.org',
        # Thêm URL bạn muốn crawl
    ]

    data = crawl_multiple_pages(urls)
    if data:
        save_to_json(data, 'data/output.json')
        print(f"Đã lưu dữ liệu của {len(data)} trang vào data/output.json")
    else:
        print("Không thu thập được dữ liệu nào.")

if __name__ == "__main__":
    main()

