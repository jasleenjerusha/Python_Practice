def greet():
    print("Hello")

greet()

def greet(name,time):
    print(f'Good {time} {name}')

greet('Jerusha','Morning')

print("*****")

def greet(name,time):
    print(f'Good {time} {name}')

name = input("Ënter your name: ")
time = input("Enter the time of the day:")

greet(name,time)

#Calculating the area of the circle

def area(Radius):
    print(3.142*Radius*Radius)

Radius = int(input("Enter radius of circle: "))

area(Radius)