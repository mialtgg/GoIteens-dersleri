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


    # Takvim saklamak için boş sözlük
calendar = {}

while True:
    print("\n1. Takvimi görüntüle")
    print("2. Bir etkinlik ekleyin")
    print("3. Olay silme")
    print("4. Çıkış")

    choice = input("Seçeneği seçin (1/2/3/4): ")

    if choice == "1":
        # Takvimi ve etkinlikleri görüntüleyin
        if calendar:
            print("\nTakvim:")
            for date, events in calendar.items():
                print(f"{date}: {', '.join(events)}")
        else:
            print("Takvim boş.")

    elif choice == "2":
        # Takvime bir etkinlik ekleyin
        date = input("Etkinliğin tarihini girin (gg.aa.yyyy biçiminde): ")
        event = input("Etkinliğin adını girin: ")

        # Takvime bir etkinlik ekleyin
        if date in calendar:
            calendar[date].append(event)
        else:
            calendar[date] = [event]

        print("Etkinlik takvime eklenmiştir.")

    elif choice == "3":
        # Takvimden bir etkinliği silme
        date = input("Silmek istediğiniz olayın tarihini girin (gg.aa.yyyy biçiminde): ")

        if date in calendar:
            event = input("Silmek istediğiniz olayın adını girin: ")

            if event in calendar[date]:
                calendar[date].remove(event)
                print("Etkinlik takvimden silinmiştir.")
            else:
                print("Olay bulunamadı.")
        else:
            print("Bu tarih için herhangi bir etkinlik bulunamadı.")

    elif choice == "4":
        # Uygulamadan çıkın
        print("Güle güle!")
        break

    else:
        print("Yanlış seçim. Lütfen tekrar deneyin.")
