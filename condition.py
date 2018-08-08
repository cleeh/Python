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
    
typeText = input('Type text written on prompt: ')
print(typeText)
typeText = int(input('20 will be added'))
print(typeText + 20)