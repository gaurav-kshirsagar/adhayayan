x = 10          #global variable
def fun1():
    y = 20      #local variable
    print("localy in fun1 x= ",x)
    print("localy in fun1 y= ",y)
    #print("localy in fun1 z= ",z)  Name error

def fun2():
    z= 30
    print("localy in fun2 x= ",x)
    print("localy in fun2 z= ",z)
    #print("localy in fun2 y= ",y)  Name error

fun1()
fun2()
print("gloablly, x= ",x)
#print("globally, y= ",y)   Name error
#print("gloablly, z= ",z)   Name error