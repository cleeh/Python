try:
    print(100/0)
except ZeroDivisionError:
    print('Divided by 0')
    
try:
    print("String" + 100)
except TypeError:
    print('Two object type is not matched each other')
    
try:
    string1 = "String"
    print(string1[100])
except IndexError:
    print('Index range over')
    
try:
    dic = {"1":1, "2":2}
    print(dic[3])
except KeyError:
    print('No key is matched')
finally:
    print('\'finally\' always executed')