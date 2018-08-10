sum = 0
i = 0
while i < 10:
    i = i + 1
    sum = sum + i
print('1 + 2 + ... + 10 =',sum)
print('')

for x in range(1, 11):
    print(x, end = ' ')
print('')

for a in range(1, 10):
    print(a,'Stage')
    for b in range(1, 10):
        print(a,'*',b,'=',a*b)
print('')

def plus9(a):
    return a + 9
print('plus9(10):',plus9(10))
print('')


def Add(a,b):
    return a + b
print('Add(10, 20):', Add(10, 20))
print('Add(3.14, 6.28):', Add(3.14, 6.28))
print('Add(1 + 2j, 3 + 8j):', Add(1 + 2j, 3 + 8j))
print('Add("Dog", " Wolrd"):',	 Add("Dog", " World"))