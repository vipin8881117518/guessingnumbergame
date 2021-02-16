##################----escaped  sequence----########
# print(r"this is \\ double backslash")
# print(r"this is /\/\/\ mountain")
# print(r"he is \t awsome ")
# print(r"\" \n \t \'")

# number1,number2,number3 = input("enter the number ").split(",")
# average = (int(number1)+int(number2)+int(number3))/3
# print(average)

# user_name = input("enter your name = ")
# reverse = user_name[-1::-1]
# print(f"your reverse name is {reverse}")

# name,character = input("enter your name and character ").split(",")
# print(f"length of your name is {len(name.replace(' ',''))}")
# print(f" repeate character  of your name is {name.strip().lower().count(character.strip().lower())}")

#importing the random library

# import random

# using the choice() function
# winning_number = random.choice([1,10])
# guessed_number = int(input("guess the number"))

# if(winning_number == guessed_number):
#     print("congrats ! you win")
# else:
#     if(guessed_number <= winning_number):
#         print("oops it's low ")
#     if(guessed_number >= winning_number):
#         print("oops it's high ")

# print()

# print("\r")

# name, age = input("enter your name and age comma seprated ").split(",")
# if name[0] == ("A" or "a") and (int(age) >= 10):
#     print("you can watch COCO movie")  
# else:
#     print("you can't watch this movie ")  

# number = int(input("enter your number "))
# i = 1
# total = 0
# while i<=number:
#     total = total +i
#     i +=1
# print(f"sum of your number is {total}")

# number = input("enter numbers and you'll get total ")
# total = 0
# i=0
# while i<len(number):
#     total+=int(number[i])
#     i+=1
# print(total)

# name = input("entter your name ")
# i=0
# temp_var = ""
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]}: {name.count(name[i])}")
#     i+=1

import random
winning_number = random.randint(1,100)
number = int(input("enter your number between 1 and 100 "))
guess = 1
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win , you guessed thism number {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
            guess+=1
            number = input("enter your number again ")
        else:
            print("too high")
            guess+=1
            number = input("enter your number again ")
            
