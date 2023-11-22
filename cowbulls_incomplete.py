import random

def compare_numbers(number, user_guess):
    cows=0    #initiating 2 varaibles 'cows' and 'bulls' to 0 (it is to store the value of bulls and cows)
    bulls=0
    cowbull={0:cows,1:bulls} #dictionary 'cowbull' storing value of '0' as the value of 'cows' and value of '1' as the value of 'bulls'

    for j in range(4):  #checks if the users guess is in the right place as the random number and stores the value in 'bulls' variable
        if str(user_guess[j])==str(number[j]):
            bulls+=1

    for i in list(number):  #checks if the users guess has the number in the random number
        if i in list(user_guess):
            cows+=1

    cowbull[1]=bulls #changes the value of 1 in the dictionary 'cowbull'
    cowbull[0]=cows #changes the value of 0 in the dictionary 'cowbull' 
    
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number #changed the range of randint from '(0,9999)' to '(1000,9999)'
guesses = 0
#print(number) #added parenthesis around 'number'

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #removed 'raw_' from 'raw_input'
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + " guess! The number was "+str(number)) #added 'guess' before '!' mark
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
