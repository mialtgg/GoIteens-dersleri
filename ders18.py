import matplotlib.pyplot as plt
import numpy as np
import random
x = np.linspace(-10, 10, 100)
y = 2 * x + 1
plt.plot(x, y)
plt.title("y = 2x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


gizli_sayi = random.randint(1, 10)

print("1 ile 10 arasında bir sayı tahmin edin!")

while True:
  
        tahmin = int(input("Tahmininiz: "))

        if tahmin == gizli_sayi:
            print("🎉 Tebrikler! Doğru tahmin ettiniz!")
            break
        elif tahmin < gizli_sayi:
            print("Daha büyük bir sayı tahmin edin.")
        else:
            print("Daha küçük bir sayı tahmin edin.")
