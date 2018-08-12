volume = {'truedew':360,'goodday':360,'hanrasan':375}
print('volume:',volume)
print('volume[\'goodday\']:',volume['goodday'])
print('len(volume):',len(volume))
del volume['hanrasan']
print('del volume[\'hanrasan\']:',volume)