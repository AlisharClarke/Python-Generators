from random import *
print("Welcome to Command Prompt Restaurant. This will be your meal. You do not have choice here.")
aDrinks = ["Water", "Lemonade", "Iced Tea"]
#Generates a random integer.
aRandomIndex = randint(0,len(aDrinks)-1)
print("You will have a glass of:")
print(aDrinks[aRandomIndex])
aSides = ["Breadsticks", "French Fries", "Mashed Potatoes"]
#Generates a random integer.
aRandomIndex = randint(0,len(aSides)-1)
print("You will have a side of:")
print(aSides[aRandomIndex])
from random import *
aMain = ["Spaghetti", "Grilled Salmon", "Steak"]
#Generates a random integer.
aRandomIndex = randint(0,len(aMain)-1)
print("Your main course will be:")
print(aMain[aRandomIndex])
from random import *
aDessert = ["Ice Cream", "Mochi", "Pudding"]
#Generates a random integer.
aRandomIndex = randint(0,len(aMain)-1)
print("Your dessert will be:")
print(aDessert[aRandomIndex])
print("Your total cost is:")
from random import *
aRandomNumber = randint(10, 100)
print(aRandomNumber)
print("dollars. Have a good day.")
