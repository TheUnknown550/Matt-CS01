x=int(input("enter the amount of numbers you will in put: "))
arr=[]
for a in range(x):
    y= int(input("enter your input"))
    arr += [y]
print(arr)
arr.sort()
print("your array after sorting = ",arr)
print("your lowest numbers is ",arr[0])
arr.sort(reverse=True)
print("ypur highest number is ",arr[0])