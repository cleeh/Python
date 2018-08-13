text = '''Testing
writing text
in the files
'''
files = open('fileIO.txt','w')
print(files)
files.write(text)
files.close()