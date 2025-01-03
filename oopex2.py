class MyClass:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def static_method():
        print("Bu bir statik yöntemdir")

    @classmethod
    def class_method(cls):
        print("Bu bir sınıf yöntemidir")
        print("Sınıf:", cls)
# Sınıfın bir örneğini oluşturmadan statik yöntemi çağırma
MyClass.static_method() # Çıktı: Bu bir statik yöntemdir
# Sınıfın bir örneğini oluşturmadan sınıf yöntemini çağırma
MyClass.class_method() # Çıktı: Bu bir sınıf yöntemidir, Sınıf: <class '__main__.MyClass'>
# Sınıfın bir örneğini oluşturma ve yöntemleri çağırma
obj = MyClass(10)
obj.static_method() # Çıktı: Bu bir statik yöntemdir
obj.class_method() # Çıktı: Bu bir sınıf yöntemidir, Sınıf: <class '__main__.MyClass'>