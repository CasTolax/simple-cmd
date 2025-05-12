import time
import os
import getpass
import random
from datetime import datetime
import json

PASSWORD = "Can123"
LOG_DOSYA = "log.txt"

class Arayuz:
    def baslatma_animasyonu(self):
        print("program başlatılıyor...")
        time.sleep(2.4)
        print("sistem yükleniyor (kaynaklar %43)")
        time.sleep(2)
        print("yükleniyor... %65")
        time.sleep(3.2)
        print("yükleniyor. %78")
        time.sleep(2)
        print("yükleniyor.. %86")
        time.sleep(3.4)
        print("yükleniyor... %98")
        time.sleep(1.5)
        print("yüklendi. %100")

    def arayuz(self):
        while True:
            try:
                print("-- Ceaser Terminali --")
                soru = input("\nBaşlatmak için 1'e, çıkmak için 2'ye basın: ")

                if soru == "2":
                    print("Program sonlandırıldı.")
                    break
                elif soru == "1":
                    self.baslatma_animasyonu()
                    print("\nTerminale hoş geldiniz.\n")
                    Terminal().terminal_govdesi()
                    break
                else:
                    print("Geçersiz seçim, lütfen 1 veya 2 girin.")
            except Exception as e:
                print(f"Hata oluştu: {e}")

class Terminal:
    def __init__(self):
        self.baslangıc = datetime.now()
        self.komut_gecmisi = []
        self.ayarlar = {}
        self.ayarları_yukle()

    def terminal_govdesi(self):
        print("help yazarak kullanabileceğiniz komutlara bakabilirsiniz.\n")
        while True:
            try:
                gövde = input("CeaserCmd>> ").strip()
                self.komut_gecmisi.append(gövde)

                timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
                with open(LOG_DOSYA, "a", encoding="utf-8") as f:
                    f.write(f"{timestamp} {gövde}\n")

                komut = gövde.lower()

                if komut == "help":
                    self.komut_help()
                elif komut == "cd":
                    self.komut_cd()
                elif komut == "ls":
                    self.komut_ls()
                elif komut == "tinfo":
                    self.komut_tinfo()
                elif komut == "calc":
                    self.komut_calc()
                elif komut == "datetime":
                    self.uptime()
                elif komut == "info":
                    self.komut_info()
                elif komut == "timelook":
                    self.komut_timelook()
                elif komut == "log":
                    self.komut_log()
                elif komut == "log --clear":
                    self.komut_log_clear()
                elif komut == "userinfo":
                    self.komut_userinfo()
                elif komut == "clear":
                    os.system("cls" if os.name == "nt" else "clear")
                elif komut == "history":
                    self.komut_history()
                elif komut.startswith("run"):
                    self.dosyacalıstır(gövde)
                elif komut == "exit":
                    print("programdan çıkıldı")
                    break
                elif komut == "yzgame":
                    self.komut_yzgame()
                elif komut == "lucky":
                    self.komut_lucky()
                elif komut == "colorama":
                    print("sorry this isn't exists")
                else:
                    print("Geçersiz komut. 'help' yazarak komutları görebilirsiniz.")

            except Exception as e:
                print(f"Hata oluştu: {e}")

    def komut_help(self):
        print("""
Kullanabileceğiniz komutlar:
  cd         - Klasör değiştir
  tinfo      - terminal hakkında bilgiler
  clear      - sil 
  run        - dosyayı çalıştırır(.py)                       
  ls         - Dosyaları listele
  calc       - basit hesap makinesi
  datetime   - işlem zamanı veya bilgisiyar açık kalma süresi
  info       - Sistem bilgisi
  timeLook   - Şu anki zamanı göster
  log        - Kayıt sistemi | --clear (etkin)
  colorama   - Renkli yazı örneği (yok)
  userinfo   - Kullanıcı adı göster
  history    - komut geçmişi
  exit       - Terminalden çık
  yzgame     - yazı/tura şans oyunu
  lucky      - günün şanslı sayısını gösterir
""")

    def ayarları_yukle(self):
        try:
            with open("ayarlar.json", "r", encoding="utf-8") as f:
                self.ayarlar = json.load(f)
                print("ayarlar yüklendi")
        except FileNotFoundError:
            print("ayar dosyası bulunamadı")
            self.ayarlar = {"tema": "koyu", "log": True}
        except json.JSONDecodeError:
            print("ayar dosyası bozuk. varsayılanlar yüklendi")
            self.ayarlar = {"tema": "koyu", "log": True}

    def ayarları_kaydet(self):
        with open("ayarlar.json", "w", encoding="utf-8") as f:
            json.dump(self.ayarlar, f, indent=4, ensure_ascii=False)
            print("ayarlar kaydedildi")

    def komut_cd(self):
        secim = input("gitmek istediğiniz dosya: ").strip()
        klasorler = ["downloads_file", "files", "documents_file", "saves_file"]
        if secim in klasorler:
            print(f"{secim} dosyasına geçildi")
        else:
            print("hata: yanlış veya olmayan dosya")

    def dosyacalıstır(self, komut):
        dosya_adi = komut[4:].strip()
        if not dosya_adi.endswith(".py"):
            print("sadece .py uzantılı dosyalar çalıştırılabilir")
        elif not os.path.exists(dosya_adi):
            print(f"hata: {dosya_adi} dosyası bulunamadı")
        else:
            print(f"{dosya_adi} çalıştırılıyor...\n")
            os.system(f"python {dosya_adi}")

    def komut_ls(self):
        print("""
--files--
    downloads_file
    files
    documents_file
    saves_file""")

    def komut_calc(self):
        hesap = input("hesaplamak istediğiniz işlemi giriniz (ör: 2+2): ")
        if all(c in "0123456789+-*/(). " for c in hesap):
            try:
                print(eval(hesap))
            except:
                print("işlem hatalı")
        else:
            print("geçersiz karakter")

    def uptime(self):
        suan = datetime.now()
        fark = suan - self.baslangıc
        saat, kalan = divmod(fark.seconds, 3600)
        dakika, saniye = divmod(kalan, 60)
        print(f"program açık kalma süresi: {fark.days} gün, {saat} saat, {dakika} dakika, {saniye} saniye")

    def komut_tinfo(self):
        print("kuruluş zamanı: 4 mayıs \n dev:CanCeaser \n")

    def komut_info(self):
        print("--sistem bilgileri--")
        print(f"OS Adı: {os.name}")
        try:
            print(os.uname())
        except AttributeError:
            print("uname() bu sistemde desteklenmiyor.")
        print(f"PATH: {os.getenv('PATH')}")
        print("kullanılan terminal türü: Ceaser Terminal")

    def komut_timelook(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Güncel zaman: {current_time}")

    def komut_log(self):
        sifre = input("şifreniz: ")
        if sifre == PASSWORD:
            print("log erişimi verildi")
            if os.path.exists(LOG_DOSYA):
                with open(LOG_DOSYA, "r", encoding="utf-8") as f:
                    icerik = f.read()
                    if icerik.strip():
                        print("-- log kayıtları --")
                        print(icerik)
                    else:
                        print("log boş")
            else:
                print("henüz log oluşturulmadı")
        else:
            print("yanlış şifre")

    def komut_log_clear(self):
        if os.path.exists(LOG_DOSYA):
            open(LOG_DOSYA, "w").close()
            print("log temizlendi")
        else:
            print("log dosyası bulunamadı")

    def komut_userinfo(self):
        username = getpass.getuser()
        print(f"Kullanıcı adı: {username}")

    def komut_history(self):
        if self.komut_gecmisi:
            print("-- KOMUT GEÇMİŞİ --")
            for i, cmd in enumerate(self.komut_gecmisi, 1):
                print(f"{i}. {cmd}")
        else:
            print("henüz komut geçmişi yok")

    def komut_yzgame(self):
        while True:
            secenekler = ["yazı", "tura"]
            soru = input("Yazı mı Tura mı? (çıkmak için 'exit'): ").strip().lower()

            if soru == "exit":
                print("Yazı tura oyunu kapatıldı.")
                break
            elif soru not in secenekler:
                print("Lütfen sadece 'yazı' veya 'tura' yazın.")
                continue

            sans = random.choice(secenekler)
            if soru == sans:
                print(f" Tebrikler! Bildiniz: Çıkan sonuç -> {sans}")
            else:
                print(f" Maalesef, bilemediniz. Seçiminiz: {soru}, Çıkan: {sans}")

    def komut_lucky(self):
        sayi = random.randint(1, 100)
        print(f"{sayi} şanslı sayınız.")

if __name__ == "__main__":
    arayuz = Arayuz()
    arayuz.arayuz()
