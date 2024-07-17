import requests
from time import sleep

def download_urls(urls, max_retries=4):
    results = {}
    
    for url in urls:
        attempt = 0
        while attempt < max_retries:
            try:
                res = requests.get(url)
                res.raise_for_status()
                results[url] = res.content.decode('utf-8')
                break
            except requests.exceptions.RequestException as e:
                attempt += 1
                if attempt == max_retries:
                    results[url] = f"Error downloading {url}: {str(e)}"
                else:
                    sleep(2)
    
    return results
urls = ['https://example.com'

]

results = download_urls(urls)
for url, content in results.items():
    print(f"URL: {url}")
    if content.startswith("Error"):
        print(content)
    else:
        print(f"Content: {content[:50]}...")
    print()
