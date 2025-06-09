menü = """
        -Python Kütüphanesine Hoş Geldiniz-
    
    1) Kitap Ver
    2) Kitap Al
    3) Tümünü Listele
    Q) Çıkış     
    

"""
liste = list()
def kitapver(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Verdiğiniz kitap için teşekkür ederiz...")
def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapal(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitabı başarıyla aldınız, iyi okumalar...")
    else:
        print("İstediğiniz kitap mevcut değildir!")
def listele(liste:list):
    for a in liste:
        print("Kitap Adı : {}       Yazar Adı : {}".format(a[1],a[0]))
while True:
    print(menü)
    secim = input("İşlem numarasını giriniz : ")

    if secim=="1":
        yazar = input("Yazar adı : ")
        kitap_adi = input("Kitap adı : ")
        kitap = (yazar,kitap_adi)
        kitapver(kitap,liste)
    elif secim=="2":
        yazar = input("Yazar adı : ")
        kitap_adi = input("Kitap adı : ")
        kitap = (yazar, kitap_adi)
        kitapal(kitap,liste)
    elif secim=="3":
        listele(liste)
    elif secim=="Q" or secim=="q":
        print("Çıkış yapılıyor...")
        quit()
    else:
        print("Hatalı seçim yaptınız!")
    input("Ana menüye dönmek için enter'a basınız...")