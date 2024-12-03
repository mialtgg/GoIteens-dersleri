ogrenciler = {
    "Ali": {
        "yas": 17,
        "dersler": ["Matematik", "Fizik"],
        "notlar": [85, 90]
        },
    "Ayşe": {
        "yas": 16,
        "dersler": ["Türkçe", "Coğrafya"],
        "notlar": [95, 88]
        }
}

while True:
    komut = input("Komut giriniz (ekle, listele, sil, not değiştir, çık): ")
    
    if komut == "ekle":
        name = input("Adı: ")
        yas = int(input("Yaş: "))
        dersler = input("Dersler: ").split(", ")
        notlar = list(map(int, input("Notlar: ").split(", ")))
        ogrenciler[name] = {"yas": yas, "dersler": dersler, "notlar": notlar}
    
    elif komut == "sil":
        name = input("Adı: ")
        ogrenciler.pop(name, None)  # Öğrenciyi silme
    
    elif komut == "listele":
        for name, data in ogrenciler.items():
            print(ogrenciler)
    
    elif komut == "not değiştir":
        name = input("Adı: ")
        if name in ogrenciler:
            ders = input("Ders: ")
            index = ogrenciler[name]["dersler"].index(ders)
            yeni_not = int(input("Yeni not: "))
            ogrenciler[name]["notlar"][index] = yeni_not
    
    elif komut == "çık":
        break
    else:
        print("Bilinmeyen komut.")
