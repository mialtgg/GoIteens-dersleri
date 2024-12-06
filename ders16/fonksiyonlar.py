def print_message():
    print('Mine ALTUĞ')
    print("hello dünya")   
    
print_message()
print_message()

def print_sum():
    a = 7
    b = 9
    print(a+b)   
    
print_sum()

def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*' * 10)      
draw_box()
def draw_triangle():
  for i in range(10):  # 10 kez çiz
    i = i + 1    # +1 değeri her seferinde eklenecek
    print('*' * i) # 1 yıldız + yeni değer
    
draw_triangle()

def greeting(last_name):
    print('hello', last_name)
    
greeting('Adar')
greeting('Tok')