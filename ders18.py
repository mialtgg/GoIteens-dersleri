# Birinci yöntem: 'open' ve 'close' ile dosya yazma
file = open('example.txt', 'w')  # Dosyayı yazma modunda açıyoruz
file.write("Bu bir yazma komutudur\n")  # İlk satırı yazıyoruz
file.write("Bu satır da dosyaya yazılacak")  # İkinci satırı yazıyoruz
file.close()  # Dosyayı kapatıyoruz

# Dosyanın içeriğini ekrana yazdırma
with open('example.txt', 'r') as file:  # Dosyayı okuma modunda açıyoruz
    content = file.read()  # Dosyanın içeriğini okuyoruz
    print(content)  # İçeriği ekrana yazdırıyoruz

# İkinci yöntem: 'with' bloğu kullanarak dosya yazma
with open("example.txt", "w") as file:  # Dosyayı yazma modunda açıyoruz
    file.write("Hi there!")  # Dosya üzerinde işlemi gerçekleştiriyoruz

# Dosyanın içeriğini ekrana yazdırma
with open('example.txt', 'r') as file:  # Dosyayı okuma modunda açıyoruz
    content = file.read()  # Dosyanın içeriğini okuyoruz
    print(content)  # İçeriği ekrana yazdırıyoruz
