# Hp Fiyat Takip Botu

Bot çalıştırıldığında verilen url adresine gitmekte; verilen url'deki **ürünün adını**, **ürünün fiyatını** ve **tarih-saat bilgisini** `.txt` dosyasına sıralı olarak yazmaktadır. Txt dosyası **database** görevi görmekte.

Bot yazdığı dosyadan okuma yaparak kayıt ettiği **en yüksek fiyat**, **en düşük fiyat** ve **çalıştırıldığı andaki fiyatını** kullanıcıya göstermektedir.

Bu script Python'un requests ve BeautifulSoup modüllerini kullanmaktadır. BeautifulSoup modülünün indirilmesi gerekmetedir.
BeautifulSoup modülünü indirmek için: `pip install beautifulsoup4`

BeautifulSoup hakkında detaylı bilgi için: <https://pypi.org/project/beautifulsoup4/>

## Dosyadan Çoklu Ürün Takibi

`hpFiyatTakip_multipleFromFile.py` adlı script ile tek bir dosyaya girilen linklerin otomatik kontrol edilmesi özelliği kazandırılmıştır.

Çoklu link kontrolü yapılması için url'lerin `url_file.txt` dosyasına satır satır kayıt edilmesi gerekmektedir. Bot çalıştırıldığında `url_file.txt` dosyası satır satır okunacak ve gerekli linke gidip fiyat okuması yapılacak. Gerekli bilgiler internetten çekildikten sonra `fiyat.txt` dosyasına kayıt edilecek.

Botun bir sonraki çalıştırılışında dosyadaki ürün başlığına göre fiyat karşılaştırması yapacak ve kullanıcıya **en yüksek**, **en düşük** ve **çalıştırıldığı zamanki fiyatını** yazdıracaktır.
