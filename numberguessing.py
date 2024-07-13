import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)


    if top_of_range <= 0:
        print('please type a number larger than zero next time')
        quit()
else:
    print('please type a number next time')
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

print(random_number)

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue
    
    if user_guess == random_number:
        print("you got it !")
        break
    elif user_guess > random_number:
        print("you are above the number!")
    else:
        print("you are below the number!")
         
print("you got it",guesses,"guesses")
# randrange() :
# this is the first way to generate a random number it has a starting and an ending range 
# this will include the starting range and  it will not include the ending range in the ouput
# for eg (0,11) it will generate a random number from 0 to 10 and it will not generate the number 11 in the output.

#randint:

# this is the second way to generate a random number it also has a starting and an ending range 
# In this function it will generate the starting range and it will also include an ending range 
# for eg (0,11) it will generate a random number from 0 to 11 and it will also generate the number 11 in the output








































