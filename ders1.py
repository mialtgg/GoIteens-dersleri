calisanlar = {
    "Ceren": {
        "pozisyon": "yönetici",
        "maas": 50000,
        "baslangic": "2020-0sil1-01"
    },
    "Demet": {
        "pozisyon": "developer",
        "maas": 40000,
        "baslagic": "2020-02-01"
    }
}

while True:
    komut=input("Komut giriniz:(ekle,sil,listele,maaş_değiştir,çık)")
    if komut== "ekle":
        isim =input("Adı girin")
        pozisyon = input("Pozisyonu ne ")
        maas = input("maaş")
        baslanic=input("tarihi ne")
    elif komut=="sil":
        if isim in calisanlar:
         isim=input("kullanıcı ismi")
         del calisanlar[isim]
        else:
           print("çalışan yok ")
    elif komut=="listele":
       for key,value in calisanlar.items():
          print(isim)
    elif komut=="maaş_değiştir":
       isim=input("adı ne")
       current_maas=calisanlar[isim]["maas"]
       yeni_maas=int(input("maaş girin"))
       calisanlar[isim]["maas"]=yeni_maas
       print("maaş değiştirildi")

    elif komut == "çık":
       break
    else:
       print("böyle bir komut yok")   
print(calisanlar)