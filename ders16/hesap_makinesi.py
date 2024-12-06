def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def uslu_hesaplama(a, b):
    return a ** b

def carpma(a, b):
    return a * b

def hesapla(islem_A, islem_B, islem):
    if islem not in ['+', '-', '*', '^']:
        print('Bilinmeyen işlem')
    else:
        if islem == '+':
            sonuc = toplama(islem_A, islem_B)
        elif islem == '-':  
            sonuc = cikarma(islem_A, islem_B)
        elif islem == '*':
            sonuc = carpma(islem_A, islem_B)
        else:
            sonuc = uslu_hesaplama(islem_A, islem_B)
        
        print(islem_A, islem, islem_B, '=', sonuc)
    
a, operator, b = input('Bir işlem giriniz (örneğin: 5 + 3): ').split()
hesapla(int(a), int(b), operator)
