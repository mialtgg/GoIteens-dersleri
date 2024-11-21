# Boş bir dictionary oluşturuyoruz
favori_filmler = {}

# Kullanıcıyı karşılıyoruz ve başlangıç verilerini girme isteği yapıyoruz
print("Favori Filmlerini ve Puanlarını Girebileceğin Bir Programa Hoş Geldin!")
print("Başlamak için 3 tane favori filmini ve puanlarını gir.")

# Kullanıcıdan 3 favori film ve puanlarını alıyoruz
for i in range(3):
    film = input(str(i + 1) + ". Filmin adı: ")  # Filmin adı giriliyor
    puan = int(input(film + " için puanın (1-10 arasında): "))  # Filmin puanı giriliyor
    favori_filmler[film] = puan  # Film adı anahtar, puan değeri olarak dictionary'e ekleniyor

# Başlangıç verileri kullanıcıya gösteriliyor
print("\nFavori Filmler ve Puanların:")
print(favori_filmler)  # Dictionary'deki tüm filmler ve puanlar ekrana yazdırılıyor

# Güncelleme menüsü sürekli çalışacak şekilde başlatılıyor
while True:
    print("\nNe yapmak istersin?")
    print("1 - Yeni bir film ekle")  # Yeni film ekleme seçeneği
    print("2 - Bir filmin puanını güncelle")  # Bir filmin puanını güncelleme seçeneği
    print("3 - Bir filmi sil")  # Bir filmi silme seçeneği
    print("4 - Tüm filmleri gör")  # Tüm filmleri görme seçeneği
    print("5 - Çıkış")  # Çıkış yapma seçeneği

    # Kullanıcının yaptığı seçim alınır
    secim = input("Seçimin (1-5): ")

    if secim == "1":
        # Yeni film ekleme
        yeni_film = input("Yeni filmin adı: ")  # Yeni filmin adı alınır
        yeni_puan = int(input(yeni_film + " için puanın (1-10 arasında): "))  # Yeni filmin puanı alınır
        favori_filmler[yeni_film] = yeni_puan  # Yeni film ve puan dictionary'ye eklenir
        print("\n" + yeni_film + " başarıyla eklendi!")  # Eklenen film bilgisi ekrana yazdırılır

    elif secim == "2":
        # Filmin puanını güncelleme
        film_guncelle = input("Puanını güncellemek istediğin filmin adı: ")  # Güncellenmek istenen film alınır
        if film_guncelle in favori_filmler:  # Eğer film listede varsa
            yeni_puan = int(input(film_guncelle + " için yeni puan (1-10 arasında): "))  # Yeni puan alınır
            favori_filmler[film_guncelle] = yeni_puan  # Film güncellenir
            print("\n" + film_guncelle + "'nin puanı güncellendi!")  # Güncellenen film bilgisi yazdırılır
        else:
            print("\n" + film_guncelle + " listede bulunamadı!")  # Film listede yoksa mesaj yazdırılır

    elif secim == "3":
        # Film silme
        film_sil = input("Silmek istediğin filmin adı: ")  # Silinmek istenen film alınır
        if film_sil in favori_filmler:  # Eğer film listede varsa
            del favori_filmler[film_sil]  # Film dictionary'den silinir
            print("\n" + film_sil + " başarıyla silindi!")  # Silinen film bilgisi yazdırılır
        else:
            print("\n" + film_sil + " listede bulunamadı!")  # Film listede yoksa mesaj yazdırılır

    elif secim == "4":
        # Tüm filmleri listeleme
        print("\nFavori Filmlerin ve Puanların:")
        for film, puan in favori_filmler.items():  # Dictionary'deki tüm filmler ve puanlar sırasıyla yazdırılır
            print(film + ": " + str(puan) + " puan")

    elif secim == "5":
        # Çıkış
        print("\nProgramdan çıkılıyor. Görüşmek üzere!")  # Çıkış mesajı
        break  # Programdan çıkılır

    else:
        print("\nGeçersiz seçim, lütfen tekrar dene.")  # Geçersiz seçim yapılırsa uyarı verilir
