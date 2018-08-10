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

print("int('100'):",int('100'))
print("a:",a)
print("bin(a):",bin(a))
print("oct(a):",oct(a))
print("hex(a):",hex(a))

a=int('19', 16)
print("int('19',16):",a)
b=int('32', 8)
print("int('32',8):",b)

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