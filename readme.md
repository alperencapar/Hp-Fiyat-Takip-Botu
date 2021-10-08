# Hp Fiyat Takip Botu

Bot çalıştırıldığında verilen url adresine gitmekte; verilen url'deki **ürünün adını**, **ürünün fiyatını** ve **tarih-saat bilgisini** `.txt` dosyasına sıralı olarak yazmaktadır. Txt dosyası **database** görevi görmekte.

Bot yazdığı dosyadan okuma yaparak kayıt ettiği **en yüksek fiyat**, **en düşük fiyat** ve **çalıştırıldığı andaki fiyatını** kullanıcıya göstermektedir.

Bu script Python'un requests ve BeautifulSoup modüllerini kullanmaktadır. BeautifulSoup modülünün indirilmesi gerekmetedir.
BeautifulSoup modülünü indirmek için: `pip install beautifulsoup4`

BeautifulSoup hakkında detaylı bilgi için: <https://pypi.org/project/beautifulsoup4/>
