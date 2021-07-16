x=float(input("enter ur first number : "))
y=float(input("enter ur first number : "))
z=int(input("what do u want to do this them\n1)add\n2)subtract\n3)multiply\n4)devide\n"))
if z==1:
    A=x+y
elif z==2:
    A=x-y
elif z==3:  
    A=x*y
elif z==4:
    A=x/y
else:
    A="error"
print("the ans is",A)