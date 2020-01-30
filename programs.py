#HELLO WORLD PROGRAM 
print("Hello World")

#USING FUNCTIIONS
def hello_world():
    print("hello world")

hello_world()

print("***********************")

#ADDITION OF TWO NUMBERS
a=5
b=10
Sum = a+b
print("sum of a and b is:",Sum)

print("***********************")

#GETTING INPUT FROM THE USER

a = int(input("Enter any number: "))
b = int(input("Enter second number: "))
Sum = a + b
print(f'Addition of {a} and {b} is',Sum)

print("***********************")

#USING FUNCTIONS 
def addition(num1,num2):
    print(num1+num2)

num1 = int(input("Enter any number: "))
num2 = int(input("Enter second number: ")) 

addition(num1,num2)

print("***********************")

#SQUARE ROOTS
num = 6.25
sqrt = num ** 0.5
print(f'Square root of {num} is',sqrt)

#USING FUNCTIONS
import cmath
def Sqrt(num):
    num_sqrt = cmath.sqrt(num)
    print(f'Square root of {num} is',sqrt)
num = float(input("Enter any number: "))
Sqrt(num)