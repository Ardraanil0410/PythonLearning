num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))
if num1 and num2 <0:
    print("Please enter a valid positive number")
    if num1 and num2 not int:
        print("Enter only numbers")
#addition
sum=num1+num2
print(sum)

#multiplication
product=num1*num2
print(product)

#subraction
if num1<num2:
    print(num2-num1)
else:
    print(num1-num2)

#division
if num1>num2:
    print(num1/num2)
else:
    print(num2/num1)
