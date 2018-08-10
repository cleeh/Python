a=19
b=0o23
c=0x13
d=0b10011
print(a,b,c,d)
print(type(a))
print(isinstance(a, int))
print(isinstance(b, int))
print(isinstance(c, int))
print(isinstance(d, int))
print('')

print("int('100'):",int('100'))
print("a:",a)
print("bin(a):",bin(a))
print("oct(a):",oct(a))
print("hex(a):",hex(a))
print('')

a=int('19', 16)
print("int('19',16):",a)
b=int('32', 8)
print("int('32',8):",b)
print('')

class calculator:
    def mul(x, y):
        return x * y
    
    @staticmethod
    def add(x, y):
        return x + y
    
    result = 0
    @classmethod
    def total(x, y):
        x.result = x.result + y
        return x.result
print(calculator.mul(10, 20))
print(calculator.add(10, 20))
print(calculator.total(10))
print('')

stringa = 'abcdefghi'
print('stringa:',stringa)
print('stringa[0]:',stringa[0])
print('stringa[5]:',stringa[5])
print('stringa[8]:',stringa[8])
print('stringa[-1]:',stringa[-1])
print('stringa[0:3]:',stringa[0:3])
print('stringa[1:3]:',stringa[1:3])
print('stringa[0:8]',stringa[0:8])
print('stringa[:-1]:',stringa[:-1])
print('')

stringb = 'ice'
stringc = ' '
stringd = 'cream'
print('stringb + stringc + stringd:',stringb + stringc + stringd)
print('')

print('stringb * 5:',stringb * 5)
print('')

print('"eam" in stringd:',"eam" in stringd)
print('"ice" in stringd:',"ice" in stringd)
print('')

twostringa='''fighting
today'''
twostringb='''fighting \
today'''
print('twostringa:',twostringa)
print('twostringb:',twostringb)
print('')

string1 = 'Stay hungry, Stay foolish'
print('string1:',string1)
print('string1.count("Stay"):',string1.count("Stay"))
print('string1.find("Stay"):',string1.find("Stay"))
print('string1.find("Stay",1):',string1.find("Stay",1))
print('string1.find("no"):',string1.find("no"))
print('string1.rindex("Stay"):',string1.rindex("Stay"))
print('')

string2 = ' Stay hungry '
print('string2:',string2)
print('string2.strip():',string2.strip())
print('string2 after strip():',string2)
print('string2.rstrip():',string2.rstrip())
print('string2.lstrip():',string2.lstrip())
print('string2.replace("hungry", "follish"):',string2.replace("hungry", "follish"))
print('')

string3 = ' Stay hungry '
print('string3:', string3)
print('string3.split():',string3.split())
print('string3.split("h"):',string3.split("h"))
print('"and".join(string3.split()):'," and ".join(string3.split()))