#WAP to print calculate the factorial of num entered through keyboard?
num=int(input("enter the num="))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
