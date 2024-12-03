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
