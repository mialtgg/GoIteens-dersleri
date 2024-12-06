import random

def generate_random_number():
    return random.randint(1, 100)



def random_number_check():
    number = random.randint(1, 100)  # 1 ile 100 arasında rastgele bir sayı üret
    print(f"Oluşturulan sayı: {number}")
    
    if number > 50:
        print("Bu sayı 50'den büyük.")
    elif number == 50:
        print("Bu sayı tam olarak 50.")
    else:
        print("Bu sayı 50'den küçük.")
random_number_check()


def user_status(age, is_member):
    if age < 18:
        if is_member:
            return "Reşit değilsiniz, ancak üyesiniz. Genç üyelerimize özel kampanyalara göz atabilirsiniz."
        else:
            return "Reşit değilsiniz ve üye değilsiniz. Üye olarak gençlere özel fırsatlardan yararlanabilirsiniz."
    else:
        if is_member:
            return "Yetişkinsiniz ve üyesiniz. Tüm özelliklerimize erişebilirsiniz."
        else:
            return "Yetişkinsiniz, ancak üye değilsiniz. Üye olarak daha fazla avantaj elde edebilirsiniz."

print(user_status(16, False))

def total():
    a=10
    b=30
    c=a-b
    return c
print(total())

def sum_check_with_params(num1, num2):
    total = num1 + num2
    print(f"Sayıların toplamı: {total}")
    
    if total > 100:
        print("Toplam 100’den büyük.")
    elif total == 100:
        print("Toplam tam olarak 100.")
    else:
        print("Toplam 100’den küçük.")


def add_numbers(a, b):
    total = a + b
    return total


def check_even_or_odd(total):
    if total % 2 == 0:
        print(f"Sonuç {total}, bir çift sayıdır.")
    else:
        print(f"Sonuç {total}, bir tek sayıdır.")

sum_result = add_numbers(15, 25)  
check_even_or_odd(sum_result)  
