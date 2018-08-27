class calisan:

    katsayi = 5

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

personel1 = calisan("ali","demir",2500)

personel2 = calisan ("kerim","bakir",1950)

print(calisan.tamad(personel1))
print(calisan.katsayi)