# File Handling:
'''
# Read mode:
fh = open("C:/Users/Gaurav/Desktop/Py_Adhyan/fhdemo.txt","r")

print("File opened")

#print(fh.read())
print(fh.readline(4))

fh.close()
print("file closed")


# Write and append mode:

#fh = open("gsk.txt","w")
fh = open("gsk.txt","a")

print("File opened")

fh.write("\nLine2 word10")
print("data written")

fh.close()
print("file closed")


# File creation and write "X" mode:

fh = open("C:/Users/Gaurav/Desktop/Py_Adhyan/fhdemo2.txt","x")
print("File opened")

fh.write("\n Hello I am learning file handling")

fh.close()
print("file closed")

'''

fh = open("C:/Users/Gaurav/Desktop/Py_Adhyan/fhdemo3.txt","x")
print("File opened")

#fh.write("\n Hello I am learning file handling")

fh.close()
print("file closed")


