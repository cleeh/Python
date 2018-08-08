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