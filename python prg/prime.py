num=int(input("Enter any Number :"))
flag=0
if (num==1):
    print(num," is not prime number")
elif (num>=2):
    for i in range(2,num):
        if (num%i==0):
            flag=1
            break
    if (flag==0):
        print("This is prime number")
    else:
        print("This is not prime number")
