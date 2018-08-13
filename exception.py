try:
    print(100/0)
except ZeroDivisionError:
    print('Divided by 0')
    
try:
    print("String" + 100)
except TypeError:
    print('Two object type is not matchec each other')