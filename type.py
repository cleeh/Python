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