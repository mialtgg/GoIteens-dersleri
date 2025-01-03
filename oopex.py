class Ogrenci:
    
    okul_adi = "GoITeens"
    sinifi="1-A"

    # Bir yöntem (method) tanımlıyoruz
    def selam_ver(self, isim):
        print(f"Merhaba {isim}, {self.okul_adi}'e hoş geldin!")

# Ogrenci sınıfından bir nesne oluşturuyoruz
ogrenci1 = Ogrenci()

# Yöntemi çağırıyoruz
ogrenci1.selam_ver("Ali")


# "self", "Bu nesneyi kastediyorum!" demek gibidir.
# Örneğin, sınıfın içindeki bir özelliğe ya da yönteme ulaşmak istiyorsak, self'i kullanmamız gerekir.class Rectangle:

# "self" ile Birden Fazla Nesne
# self kullanarak birçok dikdörtgen yapabilir ve hepsini ayrı ayrı yönetebiliriz:
class Rectangle:
    def __init__(width, height):  # self yok
        width = width  # Hangi nesneye ait belli değil
        height = height
        
#print(rectangle1.width)  # Hata verir, çünkü 'width' nesneye ait değil.


rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(7, 4)

print(rectangle1.width)  # Çıktı: 5
print(rectangle2.height)  # Çıktı: 4


#self, özelliklerin nesneye ait olduğunu Python'a söyler. Eğer self kullanmazsanız, özellikler sadece geçici bir değişken olur ve nesnelerle ilişkilendirilmez.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
# "Rectangle" sınıfından bir örnek oluşturulması
rectangle = Rectangle(5, 3)
# Dinamik olarak "width" niteliğinin değiştirilmesi
print("Başlangıç genişliği: ", rectangle.width) # Çıktı: 5
rectangle.width = 8
print("Değiştirilen genişlik: ", rectangle.width) # Çıktı: 8
# Nesne türünün dinamik olarak değiştirilmesi
rectangle = "Bu bir dize"
print("Değiştirilen nesne türü:", type(rectangle)) # Çıktı: <class 'str'>0