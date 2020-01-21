num1 = 3.1425467
num2 = 10.290394

#GENERAL FORMAT
print("num1 is",num1,"num2 is",num2)


# FORMAT METHOD
print('num1 is {0} and num2 is {1}'.format(num1,num2))

#OR----- TO PRINT ONLY 3 DIGITS OUTPUT
print('num1 is {0:.3} and num2 is {1:.3}'.format(num1,num2))

#OR----- TO PRINT ONLY 3 DIGITS AFTER DECIMAL POINT
print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1,num2))
 
#OR----- USING F-STRING 
print(f'num1 is {num1} and num2 is {num2}')

#OR----- USING F-STRING WITH 3 DECIMAL DIGITS
print(f'num1 is {num1:.3f} and num2 is {num2:.3f}')
