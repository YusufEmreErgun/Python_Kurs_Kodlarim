def Selamla(isim):
    print("Merhaba",isim)
    print("----------------------------------------------------------------")
"""Selamla fonksiyonunda isim parametresi kullandık. fakat selamla fonksiyonunu çalıştırırken
 isim parametresine değer atamaz isek fonksiyonumuz çalışmaz"""
def Selamla2(isim="İsimsiz"):
    print("Merhaba",isim)
    print("----------------------------------------------------------------")
# Burada eğer kullanıcı isim parametresine değer atamaz ise fonksiyonumuz varsayılan olarak "İsimsiz" değerini alır ve çalışır.
Selamla2() #İsimsiz
Selamla2("Yusuf") #Yusuf
"""Bu çalışma şeklini göstermek için örnek bir parametre uygulaması yapıyorum alt kısımda. """
def obskullanici(ad="İsimsiz",soyad="Soyisimsiz",numara="Numarasız",tc="TC'siz"):
    print("Ad:",ad)
    print("Soyad:",soyad)
    print("Numara:",numara)
    print("TC:",tc)
    print("----------------------------------------------------------------")
obskullanici("Yusuf","Ergün","24053035005","12312312311")

obskullanici("Yusuf","Ergün","24053035005")
"""sep='' parametresi ile print fonksiyonunda yazdırma işlemi sırasında araya istediğimiz karakteri koyabiliriz."""