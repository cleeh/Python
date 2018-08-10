class firstClass:
    a=1
    b=2
print(dir(firstClass))
del firstClass.b
print(dir(firstClass))
print('')

print(firstClass.a)
classA = firstClass()
classA.a = 100
classB = firstClass()
classB.a = 200
print(classA.a)
print(classB.a)