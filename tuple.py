tuple = ("Stay","hungry",0,2)
print('Original tuple:\n',tuple)
print('tuple[0], tuple[3]:\n',tuple[0],tuple[3])
print('tuple[2:4]:\n',tuple[2:4])
print('tuple + (10, 20, "Stay", "foolish"):\n',tuple + (10, 20, "Stay", "foolish"))
print('tuple * 2:\n',tuple * 2)
print('len(tuple):\n',len(tuple))
print('"hungry" in tuple:\n',"hungry" in tuple)
print('')

tuple1 = ("Stay", "hungry")
tuple2 = ("Stay", "hungry", ("Stay", "foolish"))
print(tuple2[2])
print('')

print('tuple:\n',tuple)
print('list(tuple):\n',list(tuple))
list = list(tuple)
list[1] = "foolish"
print("list = list(tuple)")
print('list[1] = "foolish":\n',list)
print('')

# Case: Return values more than two
def addmul(a,b):
    return a + b, a * b
# Case: When tuple values are used for arguments of function
arguments = (100, 200)
print('addmul(*(100, 200)):',addmul(*arguments))
# Case: Format String is used
print("%d %f %s" % (1000, 3.141592, "Stay foolish"))