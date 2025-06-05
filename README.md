Language Count Top Language Last Commit License Status Contributions
# XSS-Test-Tool
Tersine Mühendislik - FİNAL Projesi 

Farklı XSS payload’larını otomatik olarak test eden bir araç. Bir URL'ye gidip param=value yerine 50'den fazla XSS payload'ı dener. Başarılı olursa "vulnerable" olarak raporlar.

## Features / Özellikler
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

## Team / Ekip
2320191038 - Enis Seha Toprak: Geliştirici / Otomasyon
2320191019 - Salih Sefa Korkmaz: Payload / Güvenlik Araştırması & Raporlama

## Roadmap / Yol Haritası
See our plans in ROADMAP.md
Yolculuğu görmek için ROADMAP.md dosyasına göz atın.

## Research / Araştırmalar

| Topic / Başlık                    | Link                                       | Description / Açıklama                                                               |
|----------------------------------|--------------------------------------------|---------------------------------------------------------------------------------------|
| XSS Payload Analizi              | [researchs/xss-payload-analysis.md](researchs/xss-payload-analysis.md)          | Farklı XSS payload’larının karşılaştırmalı analizi. / XSS payload’larının detaylı incelemesi. |
| DOM XSS İncelemesi               | [researchs/dom-xss.md](researchs/dom-xss.md)                       | DOM tabanlı XSS açıklarının yapısı ve test yöntemleri. / DOM XSS zafiyetlerinin teknik çözümlemesi. |
| Playwright vs Selenium Karşılaştırması | [researchs/browser-tools-comparison.md](researchs/browser-tools-comparison.md)  | XSS testlerinde kullanılan iki otomasyon aracının farkları. / Tarayıcı otomasyonu araçlarının değerlendirilmesi. |
| Add More Research                | *Link to your other research files*        | *Description of the research*                                                         |

## Installation / Kurulum

### 📥 Clone the Repository / Depoyu Klonlayın


git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

🧪 Set Up Virtual Environment / Sanal Ortam Kurulumu (Önerilen)
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

pip install -r requirements.txt


## 🚀 Usage / Kullanım

Aşağıdaki adımları takip ederek XSS tarama aracınızı çalıştırabilirsiniz:

📝 Prepare Input / Giriş Verisini Hazırlayın
Test etmek istediğiniz URL’yi belirleyin. Tarama yapılacak parametreyi * karakteriyle belirtin.
Örnek: http://example.com/search?query=*

Run with Arguments / Betiği Argümanlarla Çalıştırın
Kullanılabilecek temel argümanlar:

--url: Test edilecek URL (parametresi * olan)

--browser: Tarayıcı otomasyonu seçimi (playwright veya selenium)

--output: Sonuçların kaydedileceği dosya adı

Örnek komut: python main.py --url "http://test.com/index.php?q=*" --browser selenium --output results.txt

Check the Output / Çıktıyı Kontrol Edin
Tarama sonuçları, belirttiğiniz dosyada (results.txt) yer alır.
Başarılı payload’lar ve varsa XSS türleri burada detaylı şekilde listelenir.

💡 Not: Playwright kullanıyorsanız, ilk çalıştırmadan önce aşağıdaki komutu çalıştırmayı unutmayın:
playwright install

Topluluk katkılarını memnuniyetle karşılıyoruz! Katkıda bulunmak için:

Depoyu fork'layın.

Fork’unuzu kendi bilgisayarınıza klonlayın.

Yeni bir branch oluşturun (feature/ozellik-adi).

Değişikliklerinizi yapın ve açıklayıcı commit mesajları yazın.

Değişikliklerinizi fork’unuza push edin.

Ana depoya bir Pull Request (PR) açın.

Kodlama standartlarına uyduğunuzdan emin olun (bkz: CONTRIBUTING.md).

## License / Lisans
Licensed under the MIT License.
MIT Lisansı altında lisanslanmıştır.


## Acknowledgements / Teşekkürler (Optional)
Thanks to:

Awesome Library: For enabling X.
Inspiration Source.
Special thanks to...
Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.




