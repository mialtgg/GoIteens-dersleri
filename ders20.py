import os

def read_shopping_list(file_path):
    if not os.path.exists(file_path): 
        with open(file_path, 'w') as f:  
            pass
    shopping_list = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():  # Boş satırları kontrol et
                product, quantity = line.strip().split(',')
                shopping_list[product] = int(quantity)
    print(shopping_list)  
    return shopping_list


def write_shopping_list(file_path, shopping_list):
    with open(file_path, 'w') as f:
        for product, quantity in shopping_list.items():
            f.write(f"{product},{quantity}\n")


def add_product(shopping_list):
    product = input("Ürünün adını giriniz: ")
    quantity = int(input("Ürün miktarını giriniz: "))
    shopping_list[product] = quantity
    print("Ürün eklendi.")
    file_path = "shopping_list.txt"
    write_shopping_list(file_path, shopping_list)


def delete_product(shopping_list):
    product = input("Hangi ürünü sileceksiniz? ")
    if product in shopping_list:
        del shopping_list[product]
        print(f"{product} silindi. Güncel liste: {shopping_list}")
        file_path = "shopping_list.txt"
        write_shopping_list(file_path, shopping_list)
    else:
        print("Ürün bulunamadı.")


def main():
    file_path = "shopping_list.txt"  # Dosya yolu
    shopping_list = read_shopping_list(file_path)
    while True:
        action = input("Ne yapmak istersiniz? 'ekle', 'sil' veya 'çık' yazınız: ").strip().lower()
        if action == "ekle":
            add_product(shopping_list)
        elif action == "sil":
            delete_product(shopping_list)
        elif action == "çık":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")
main()