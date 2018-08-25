baslik = "python programlama"

def metin_icerikleri(header,*args,**kwargs):

    print("başlık : ", header)

    for arguman in args:
        print(arguman)

    for metin in kwargs.items():
        print(metin)
        print(metin[0],":",metin[1])

metin_icerikleri(baslik,
                 "3", "6", "9",
                 metin1 = "merhaba dünya",
                 metin2 = "python dili",
                 metin3 = "arguman anlatimi")