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
volume = dict(temp)
print('keys:',keys)
print('values:',values)
print('temp = zip(keys, values):\n',temp)
print('volume = dict(temp):\n',volume)
print('')

print('volume:',volume)
print('volume.keys():',volume.keys())
print('volume.values():',volume.values())
print('volume.items():',volume.items())
print('volume.get(\'hanrasan\'):',volume.get('hanrasan'))
print('"goodday" in volume:',"goodday" in volume)
print('"375" in volume:', "375" in volume)
print('volume.clear():',volume.clear())
print('volume after clear():',volume)