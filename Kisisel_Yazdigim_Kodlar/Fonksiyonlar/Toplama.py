"""Python'da Toplama işlemi için yapılmıştır."""
print("Lütfen Toplamak İstediğiniz 4 Sayıyı Toplama Fonksiyonunu çalıştırdığınızda gönderdiğiniz parametreler kısmına giriniz.")
def Toplama(a,b,c,d):
    if(a>0 and b>0 and c>0 and d>0):
        print ("Girdiğiniz 4 Sayının Toplamı:",a+b+c+d)
        print("----------------------------------------------------------------")
    else:
        print("Lütfen 4 sayıyı da pozitif giriniz!!!")
        print("----------------------------------------------------------------")
Toplama(120,127,142,252)   
#Altta girdiğimiz sayılardan kaç tanesini toplamak istediğimizi belirtmeden toplama işlemi yapabiliriz. Bunun için *a parametresi kullanılır.    
def Toplama2(*a):
    toplam=0
    for i in a:
        toplam+=i
    print("Girdiğiniz Sayıların Toplamı:",toplam)
    print("----------------------------------------------------------------")
Toplama2(120,127,142,252,12,25,31,52)