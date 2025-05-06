import time
import os
import getpass  


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

    def terminal_govdesi(self):
        print("help yazarak kullanabileceğiniz komutlara bakabilirsiniz.\n")
        while True:
            try:
                gövde = input("CeaserCmd>> ").strip().lower()

                if gövde == "help":
                    print("""
Kullanabileceğiniz komutlar:
  cd         - Klasör değiştir
  ls         - Dosyaları listele
  info       - Sistem bilgisi
  timeLook   - Şu anki zamanı göster
  log        - Kayıt sistemi (yok)
  colorama   - Renkli yazı örneği (yok)
  userinfo   - Kullanıcı adı göster
  exit       - Terminalden çık
""")
                elif gövde == "cd":
                    secim = input("gitmek istediğiniz dosya: ").strip()
                    if secim == "downloads_file":
                        print("geçildi")
                    elif secim == "files":
                        print("files dosyasına geçildi")
                    elif secim == "documents_file":
                        print("documents dosyasına geçildi")
                    elif secim == "saves_file":
                        print("saves_file dosyasına geçildi")
                    else:
                        print("hata: yanlış veya olmayan dosya")

                elif gövde == "ls":
                    print("""
--files--
    downloads_file
    files
    documents_file
    saves_file""")

                elif gövde == "info":
                    print("--sistem bilgileri--")
                    print(f"OS Adı: {os.name}")
                    try:
                        print(os.uname())
                    except AttributeError:
                        print("uname() bu sistemde desteklenmiyor.")
                    print(f"PATH: {os.getenv('PATH')}")
                    print("kullanılan terminal türü: Ceaser Terminal")

                elif gövde == "timelook":
                    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    print(f"Güncel zaman: {current_time}")

                elif gövde == "log":
                    print("sorry this isn't exists")

                elif gövde == "colorama":
                    print("sorry this isn't exists")

                elif gövde == "userinfo":
                    username = getpass.getuser()
                    print(f"Kullanıcı adı: {username}")

                elif gövde == "exit":
                    print("programdan çıkıldı")
                    break

                else:
                    print("Geçersiz komut. 'help' yazarak komutları görebilirsiniz.")
            except Exception as e:
                print(f"Hata oluştu: {e}")


# Program başlat
if __name__ == "__main__":
    arayuz = Arayuz()
    arayuz.arayuz()
