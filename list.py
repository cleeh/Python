list = ["Stay", "hungry", 0, 2]

print(list[0], list[3])
print(list[2:4])
print(list + [5,1,"Newb","log"])
print(list * 2)
print(len(list))
print('')

print('Original List:\n',list)
list[2] = list[2] + 20
print('list[2] = list[2] + 20:\n',list)
list[2:4] = [777,888]
print('list[2:4] = [777,888]:\n',list)