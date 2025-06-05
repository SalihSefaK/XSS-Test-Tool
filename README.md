Language Count Top Language Last Commit License Status Contributions
# XSS-Test-Tool
Tersine Mühendislik - FİNAL Projesi 

Farklı XSS payload’larını otomatik olarak test eden bir araç. Bir URL'ye gidip param=value yerine 50'den fazla XSS payload'ı dener. Başarılı olursa "vulnerable" olarak raporlar.

# Features / Özellikler
Feature 1: Otomatik XSS Taraması
Belirtilen URL'de 50+ XSS payload’ı ile test yapar.

Feature 2: Zafiyet Tespiti
Başarılı payload'ları belirleyip "vulnerable" olarak raporlar.

Feature 3: XSS Türü Analizi
Reflected, Stored ve DOM XSS türlerini ayırt eder.

Feature 4: Tarayıcı Otomasyonu
Playwright veya Selenium ile gerçek tarayıcıda test gerçekleştirir.

Feature 5: Parametre Odaklı Test
Belirli URL parametrelerine odaklanarak tarama yapar.

Feature 6: Raporlama Desteği
Sonuçları dışa aktarır; log veya metin dosyası olarak kaydeder.

# Zafiyet Tespiti
Başarılı payload’ları tespit eder ve raporlar.

# XSS Türü Ayrımı
Reflected, Stored ve DOM XSS’i ayırt eder.

# Tarayıcı Otomasyonu
Playwright/Selenium ile gerçek tarayıcıda test yapar.

# Raporlama
Sonuçları dosyaya kaydeder, log tutar.

# Zafiyet Tespiti
Başarılı payload'ları tespit edip detaylı olarak raporlar.

# DOM XSS Desteği
Reflected, Stored ve DOM tabanlı XSS türlerini ayırarak analiz eder.

# Tarayıcı Otomasyonu
Playwright/Selenium ile gerçek tarayıcı üzerinde test desteği sağlar. (*)

Geliştirilebilirlik
Payload listesi ve tarama metodolojisi özelleştirilebilir.

Team / Ekip
219*031 - Ad Soyad: Geliştirici / Otomasyon
Ad Soyad: Payload / Güvenlik araştırması
Ad Soyad: UI/UX & Dokümantasyon
Gerektiğinde daha fazla üye ekleyin.

Roadmap / Yol Haritası
Projenin yol haritası için ROADMAP.md dosyasına göz atın.

Research / Araştırmalar
Başlık	Link	Açıklama
XSS Payload Listesi	researchs/xss-payloads.md	Kapsamlı XSS payload listesinin analizi.
DOM XSS İncelemesi	researchs/dom-xss-analysis.md	DOM XSS'e özel test yöntemleri ve tespit yolları.
Başlık	Link	Açıklama

Installation / Kurulum
Depoyu Klonlayın
bash
Kopyala
Düzenle
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git  
cd YOUR_REPO
Sanal Ortam Kurulumu (Önerilen)
bash
Kopyala
Düzenle
python -m venv venv  
source venv/bin/activate  # Windows için: venv\Scripts\activate
Bağımlılıkları Yükleyin
bash
Kopyala
Düzenle
pip install -r requirements.txt
Usage / Kullanım
Projeyi çalıştırın:

bash
Kopyala
Düzenle
python main.py --url "http://target.com/?param=*" --browser playwright --report output.txt
Adımlar:
Test edilecek URL'yi hazırlayın. (XSS test edilecek parametreyi * ile işaretleyin)

Komutu çalıştırın. --browser ile playwright veya selenium seçin.

Sonuçları output.txt içinde kontrol edin.

Contributing / Katkıda Bulunma
Topluluk katkılarına açığız! Katkı sağlamak için:

Reponun bir fork’unu oluşturun.

Fork’unuzu klonlayın:

bash
Kopyala
Düzenle
git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git
Yeni bir branch oluşturun:

bash
Kopyala
Düzenle
git checkout -b feature/yeni-ozellik
Değişiklikleri commit edin.

Fork’unuza push edin.

Pull Request açın.

Kodlama standartlarına uyduğunuzdan emin olun (bkz: CONTRIBUTING.md).

License / Lisans
MIT Lisansı altında lisanslanmıştır.

Acknowledgements / Teşekkürler
XSS Hunter ve PayloadAllTheThings projelerine ilham için.

Playwright / Selenium ekiplerine test otomasyonu desteği için.

Güvenlik araştırmaları topluluğuna teşekkürler.

Contact / İletişim
Proje Sorumlusu: Adınız veya Organizasyon - e-posta@adresiniz.com
Hata mı buldunuz? Bir issue açmaktan çekinmeyin.
