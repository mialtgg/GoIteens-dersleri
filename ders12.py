# Boş bir sözlük oluşturuyoruz
kisiler = {}

# Kullanıcıdan veri alıyoruz
print("Kişi bilgilerini giriniz.")
while True:
    isim = input("İsim: ")
    
    # Kullanıcı 'q' yazarsa, döngü sonlanır
    if isim.lower() == 'q':
        break
    
    # Yaş bilgisi alıyoruz
    yas = input(f"{isim} için yaş girin: ")
    
    # Yaşın sayısal olup olmadığını kontrol ediyoruz
    if yas.isdigit():
        kisiler[isim] = int(yas)  # Yaş bilgisini sayıya çevirip sözlüğe ekliyoruz
    else:
        print("Lütfen geçerli bir yaş girin!")

# Sözlüğü yazdırıyoruz
print("\nKişi Bilgileri:")
for isim, yas in kisiler.items():
    print(f"İsim: {isim}, Yaş: {yas}")


telefon_rehberi = {
    "Ali": "123-4567",
    "Veli": "234-5678",
    "Ayşe": "345-6789"
}
#items() Metodu: Bu metod, sözlükteki her anahtar-değer çiftini bir tuple (demet) olarak döndürür. Böylece her anahtar ve değeri ayrı ayrı işleyebilirsiniz.
print(telefon_rehberi.items())

#items() metodunu for döngüsüyle kullanarak sözlükteki her bir anahtar-değer çiftine ulaşabiliriz. Her yinelemede, bir key ve value elde ederiz.

for key, value in telefon_rehberi.items():
    print(key, ":", value)
arac_sahipleri = {
    'AA1111AA': 'Ali ATEŞ',
    'IVANOV': 'Ceyda GÜVEN',
    "AA0007AA": 'Sahra ÖZTÜRK',
    'AA007AA': 'Ali ATEŞ',
    'AB1111AB': 'Bülent KAYA',
    "AI1010KK": 'Sevda ÖZBERK',
}

# Yeni araçlar ekleniyor
arac_sahipleri['II7777AA'] = 'Özlem SU'
arac_sahipleri['АІ1234НН'] = 'Rüzgar DEREN'

# Araç numarasını arama
ara = 'AВ1111AВ'

# Araç sahibini bulma
arac_sahibi = arac_sahipleri.get(ara, '')

# Eğer araç sahibi bulunursa, sahibini yazdır
if arac_sahibi:
    print('{} - {} plakalı aracın sahibi'.format(ara, arac_sahibi))
else:
    print('{} numaralı araç bulunamadı'.format(ara))

# Aynı isme sahip araç sayısını sayma
sahipler = dict()

# Aracın sahiplerini sayıyoruz
for sahip in arac_sahipleri.values():
    if sahipler.get(sahip, 0) == 0:
        sahipler[sahip] = 1
    else:
        arac_sayisi = sahipler[sahip]
        arac_sayisi += 1
        sahipler[sahip] = arac_sayisi

# 1'den fazla aracı olan sahipleri yazdırıyoruz
for sahip, arac_sayisi in sahipler.items():
    if arac_sayisi > 1:
        print('{} sahibinin aşağıdaki sayıda arabası vardır - {}'.format(sahip, arac_sayisi))
