#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["Ada Lovelace" , "Kim Swift" , "Miral Kotb", "Madison Maxey"]
#Generates a random integer.
aRandomIndex = randint(0,len(aList)-1)
print(aList[aRandomIndex])
