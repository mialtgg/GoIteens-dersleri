calisanlar = {
    "Ceren": {
        "pozisyon": "yönetici",
        "maas": 50000,
        "baslangic": "2020-01-01"
    },
    "Demet": {
        "pozisyon": "developer",
        "maas": 40000,
        "baslagic": "2020-02-01"
    }
}

while True:  
    command = input("Komut giriniz (ekle, listele, sil, maaş değiştir , çık): ")  
    if command == "ekle":  
        name = input("Adı giriniz: ")  
        position = input("Pozisyonu giriniz: ")  
        salary = int(input("Maaşı giriniz: "))  
        start_date = input("İşe başlama tarihini giriniz (YYYY-MM-DD): ")  
        calisanlar [name] = {  
            "pozisyon": position,  
            "maas": salary,  
            "baslangic": start_date  
        }  
    elif command == "sil":  
        name = input("Adı giriniz: ")  
        if name in calisanlar:  
            del calisanlar[name]  
        else:  
            print ("Çalışan bulunamadı")  
    elif command == "listele":  
        for name, data in calisanlar.items():  
            print (name)  
            for key, value in data.items():  
                print(f" {key}: {value}")  
    elif command == "maaş değiştir":  
        name = input("Adı giriniz: ")  
        current_salary = calisanlar[name] ['salary'] 
        print (f' adlı kişinin mevcut maaşı {name} - {current_salary}')  
        new_salary = int(input('Yeni maaşı giriniz: '))  
        calisanlar[name] ['salary'] = new_salary  
        print('Başarıyla değiştirildi')  
    elif command == "çık":  
        break  
    else:  
        print ("Bilinmeyen komut")

    print(calisanlar)


     