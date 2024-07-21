print('The love calculator is calculating your score....')

name_1 = input('\nPlease enter one of your names') 
name_2 = input('\nPlease enter the name of your partner')
#________________________________________________#
combined_name = name_1 + name_2
Names_in_lowercase = combined_name .lower()

t = Names_in_lowercase . count("t")
r = Names_in_lowercase . count("r")
u = Names_in_lowercase . count("u")
e = Names_in_lowercase . count("e")

First_digit = t+r+u+e

l = Names_in_lowercase . count("l")
o = Names_in_lowercase . count("o")
v = Names_in_lowercase . count("v")
e = Names_in_lowercase . count("e")

Second_digit = l+o+v+e

score = int(str(First_digit) + str(Second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos")
elif (score >= 40) and (score <= 50):
  print(f"your score is {score}, you are alright together")
else:
  print(f"Your score is {score}.")
  