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

with open('fileIO.txt') as files:
    print(files.readline())
    print(files.readline())
    print(files.readline(4))
    files.close()

with open('fileIO.txt') as files:
    print('files.readlines():',files.readlines())
    files.close()

files = open('fileIO.txt','w+')
print('files.tell():',files.tell()) # Return Current File Pointer Location
print('files.seek(3,0):',files.seek(10)) # Set File Pointer Location
print('files.tell():',files.tell())
print('files.read():\n' + files.read())
print('files.read():\n' + files.read())
print('files.fileno():',files.fileno()) # Return File Number
files.flush() # Buffer Flush
print('files.isatty():',files.isatty()) # If 'files' is tty, return 1 or TRUE. If not, return 0 or FALSE
files.seek(5)
print('files.truncate():',files.truncate())
files.seek(0)
print('files.read():\n' + files.read())
print('files.mode:',files.mode)
print('files.name:',files.name)
print('[Before files.close()] files.closed:',files.closed)
files.close()
print('[After files.close()] files.closed:',files.closed)