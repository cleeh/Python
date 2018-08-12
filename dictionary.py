volume = {'truedew':360,'goodday':360,'hanrasan':375}
print('volume:',volume)
print('volume[\'goodday\']:',volume['goodday'])
print('len(volume):',len(volume))
del volume['hanrasan']
print('del volume[\'hanrasan\']:',volume)
print('')

keys = ['truedew','goodday','hanrasan']
values = [360,360,375]
temp = zip(keys, values)
tuple = dict(temp)
print('keys:',keys)
print('values:',values)
print('temp = zip(keys, values):\n',temp)
print('tuple = dict(temp):\n',tuple)