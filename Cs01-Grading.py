A=int(input("Enter the score the get over the year : "))
B=int(input("Enter their midterm score : "))
C=int(input("Enter their final scrore : "))
D=A+B+C
if D>=80 and D<=100:
    E="A"
elif D>=75:
    E="B+"
elif D>=70:
    E="B"
elif D>=65:
    E="C+"
elif D>=60:
    E="C"
elif D>=55:
    E="D+"
elif D>=50:
    E="D"
elif D>=0:
    E="F"
else:
    E="error"
print("their total score = ",D," which is grade ",E)