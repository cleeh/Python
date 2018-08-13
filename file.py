text = '''Testing
writing text
in the files
'''
files = open('fileIO.txt','w')
print(files)
files.write(text)
files.close()

with open('fileIO.txt', 'w', encoding = 'utf-8') as files:
    files.write("한글 만세!\n")