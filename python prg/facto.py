# funtion return withoght argument
def find_factorial():
    num=int(input("Enter a number to find factorial :"))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return (fact)
f1=find_factorial()
print("The factorial is :",f1)
