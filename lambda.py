nums = [1,2,3,4,5,6]

#NORMAL METHOD USING FUNCTIOS:
# def square(n):
#     return(n*n)


#USING LAMBDA FUNCTION:
print(list(map(lambda n: n*n ,nums)))



x = lambda a, b : a * b
print(x(5, 6))


