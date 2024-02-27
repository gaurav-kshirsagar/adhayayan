# tell(), seek()
'''
fh = open("11.txt")
print(fh.tell())

fh.seek(39)
print(fh.tell())
print(fh.readline())
fh.close()
'''

fh = open("C:/Users/Gaurav/Downloads/pylogo.jpg", "rb")
print("pylogo image is open for reading")

data = fh.read()

print("pylogo img is read and content is stored in data var")

fh.close()
print("pylogo img  closed")


nf = open("1pylogo.jpg", "xb")
print("New img created")
nf.write(data)
print("content from old img is written into new img")
nf.close()
print("New image closed")
