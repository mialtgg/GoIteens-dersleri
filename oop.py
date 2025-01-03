class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
# "Dikdörtgen" sınıfından bir örnek oluşturulması
rectangle1 = Rectangle(5, 3)
# Örnek yönteminin kullanımı
print(rectangle1.area()) # Çıktı: 15