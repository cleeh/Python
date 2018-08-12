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
list[4:4] = ["Stay","foolish"]
print('list[4:4] = ["Stay","foolish"]:\n',list)
list[4:6] = []
print('list[4:6] = []:\n',list)
del list[0]
print('del list[0]:\n',list)
print('')

list1 = ["Stay", "hungry"]
list2 = ["Stay", "hungry", ["Stay","foolish"]]
print('Overlapped List:',list2[2])
print('')

list = ["Stay", "hungry", 0, 2]
print('Original List:\n',list)
list.append(7)
print('list.append(7):\n',list)
list.insert(3,7)
print('list.insert(3,7):\n',list)
print('list.index("hungry"):\n',list.index("hungry"))
print('list.count(7):\n',list.count(7))
list.remove(7)
print('list.remove(7):\n',list)
numberlist = [50,20,100,500,200,3000,1500,10]
print('Originam numberlist:\n',numberlist)
numberlist.sort()
print('numberlist.sort():\n',numberlist)
numberlist.reverse()
print('numberlist.reverse():\n',numberlist)