x = "global variable"

def myFunc():
    x = "local variable"
    print("this is x," + x)


myFunc()
print("This is x, " + x)