chance=0
correct_num=6
while chance<5:
    guess_the_secret_num = int(input("Please enter a number between 1 and 20 : "))
    if guess_the_secret_num == 13:
        print("13 is not allowed. Try again!")
        continue
    chance+=1
    if guess_the_secret_num==correct_num:
        print("You won")
        break
    else:
        print(f"Wrong guess. You have {5 - chance} chances left.")
if guess_the_secret_num!=correct_num:
    print(f"You lost! The number was {correct_num}")






