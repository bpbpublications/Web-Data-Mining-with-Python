def greater(a,b):
  if (a>b):
    return a
  else:
    return b
 
x=5
y=7
max=greater(x,y)      #Function call with argument x and y (variables), returned value stored in max
print(max,' is greater')
print(greater(3,4),' is greater')      #Function call with constant arguments 3 and 4, value returned in print statement
