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
    files.close()

lines = ['line #1\n', 'line #2\n', 'line #3']
with open('fileIO.txt','w') as files:
    files.writelines(lines)
with open('fileIO.txt') as files:
    print(files.read())
    files.close()