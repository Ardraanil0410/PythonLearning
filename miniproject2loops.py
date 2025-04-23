even_count=0
odd_count=0
while True:
    number=int(input("Please enter the number : "))
    if number==0:
        print("End of game" )
        break
    elif number<0:
        print("This is a negative number")
        continue
    elif number%2==0:
        even_count+=1
        print("Even")
    else:
        odd_count+=1
        print("Odd")

print(f"The total number of even numbers entered are {even_count} and odd numbers are {odd_count}")


