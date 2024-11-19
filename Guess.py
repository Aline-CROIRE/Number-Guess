import random
top_range=input("Enter a maximum number : ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Enter number greater than zero next time")
        quit()
else:
    print("please type in a number next time:")
    quit()

random_number=random.randint(0,top_range)
guess=0
while True:
    guess += 1
    user_guess=int(input("Guess a number "))
    if user_guess==random_number :
        print("you got it!")
        break
    elif(user_guess>random_number):
        print("You were above the number!")
    else:
        print("You were Below the number!")
print('You got it in',guess,'guesses')



