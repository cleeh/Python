congraturationText = 'Congraturation! You have score higher than 90!'
encourageText = "It's okay. There is next chance :)"
congraturationScore = 90
getScore = 40

print('Test Score:',getScore)
if getScore >= congraturationScore:
    print(congraturationText)
else:
    print(encourageText)
print('')
    
typeText = input('Type text written on prompt:')
print(typeText)
typeText = int(input('20 will be added:'))
print(typeText + 20)
print('')

beforeInt = 20
print('beforeInt =', beforeInt)
print('<transform beforeInt into string type>')
print('beforeInt + " hours":', str(beforeInt) + ' hours')

a = 10
x = a * 2 if a > 5 else a / 2
print('a:',a)
print('(a * 2 if a > 5 else a / 2):',x)