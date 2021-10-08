import requests, datetime
from bs4 import BeautifulSoup

now = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M")

url="https://www.hepsiburada.com/asus-geforce-gtx-1650-oc-4gb-1665mhz-gddr6-dx-12-pci-express-3-0-ekran-karti-ph-gtx1650-o4gd6-p-p-HBV00000XGNBS"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50'}

def find_product_price():
    try:
        response = requests.get(url,headers=header)
    except Exception as err:
        print("Response Error: \n", err)
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #? ürünün şu anki adı ve fiyatı
    product_title = soup.find(id='product-name').get_text().strip()
    product_price = float(soup.find(id='offering-price').attrs.get('content'))
    print("Ürün: {}\n".format(product_title))
    
    #! fonksiyonception
    #? dosyaya ürün bilgisini yaz
    write_product_info_to_file(product_title,product_price)
    
    #? dosyadan ürün bilgisini oku
    productTitleAndPrice = read_product_info_from_file(product_title)
    
    #? dosyadaki fiyat bilgisi ile en yüksek, en düşük ve şu anki fiyatı bul
    find_product_minmax(productTitleAndPrice[1], product_price) #? productTitleAndPrice[1] -> [1] fiyat listesi, [0] ürün adı
    
def write_product_info_to_file(title, price):
    try:
        with open("fiyat.txt", "a", encoding="UTF-8")as file:
            file.write(title + "," + str(price) + "," + now)
            file.write("\n")
    except:
        print("\nfile write error")

def read_product_info_from_file(currentTitle):
    pricingList = []
    fileTitles = []
    with open("fiyat.txt","r", encoding="UTF-8")as file:
        for line in file:
            splitedLine = line.split(",")
            fileTitle = splitedLine[0]
            filePrice = splitedLine[1]
            fileTime = splitedLine[2]
            
            #! şu an kontrol ettiğimiz ürün ile dosyadaki okuma yaptığımız ürün aynı mı?
            if fileTitle == currentTitle:
                #? aynı ise ürün adı ve fiyatını listeye ekle
                fileTitles.append(fileTitle)
                pricingList.append(float(filePrice))
            else:
                pass
            
    #? dosyadan okunan ürün adı ve fiyatını fonksiyonu çağırdığımız yere tuple olarak döndür
    return (fileTitles, pricingList)
    #! dictionary açıp başlık ve fiyat bilgisinini ekleyebilirdik. -> dict[fileTitle] = tuple(pricingList)
        
    
#? dosyadaki fiyat bilgisi ile en yüksek, en düşük ve şu anki fiyatı karşılaştır
def find_product_minmax(productPriceList, currentPrice):
    
    minimumPrice = float(min(productPriceList))
    maximumPrice = float(max(productPriceList))
    
    #? min, max ve şu anki fiyatı kullanıcıya göster
    notifyUser(minimumPrice, maximumPrice, currentPrice)


def notifyUser(min, max, currentPrice):
    print("En Yüksek Fiyat: {}₺ \nŞu An Fiyat: {}₺ \nEn Düşük Fiyat: {}₺\n".format(max,currentPrice, min))


find_product_price()

