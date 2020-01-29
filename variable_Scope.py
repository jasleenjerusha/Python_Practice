my_name = "Jeru" #global scope variable

def print_name():
    global my_name
    my_name = "Vivek" #local scope variable
    print("the name inside the function is",my_name)

print_name()
print("Outside the fucntion name is",my_name)