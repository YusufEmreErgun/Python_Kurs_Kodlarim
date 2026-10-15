def ucle_carpma(a):
    print("1.Fonksiyon Çalıştı")
    return a*3
def dortle_carpma(a):
    print("2.Fonksiyon Çalıştı")
    return a*4
def besle_carpma(a):
    print("3.Fonksiyon Çalıştı")
    return a*5
def ikiye_bolme(a):
    print("4.Fonksiyon Çalıştı")
    return a/2
print(ikiye_bolme(besle_carpma(dortle_carpma(ucle_carpma(6)))))
#burda return değeri ile fonksiyonlar birbirine bağlanıyor ve en son return değeri ekrana yazdırılıyor.
#İç içe fonksiyon görülmüş olup return değeri ile birbirine bağlanmıştır
#Void fonksiyonlar return kullanılamazlar. Return değeri olmayan fonksiyonlar void fonksiyonlardır. Return değeri olan fonksiyonlar ise return değeri ile birbirine bağlanabilirler.