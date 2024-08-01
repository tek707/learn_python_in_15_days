# Question one  : Write a Python program to print "Hello, World!"

# Answer

print("Hello , World!")


# Question two  : Calculate the sum of two numbers entered by the user.

# Answer

# we first declear two variables called numone and numtwo
# We then prompt the user to enter the values of both numone and the numtwo variables
# Generate a new variable call sum 
# assign numone + numtwo to sum variable 
# Print out sum

numone = 0 
numtwo = 0

numone = int(input ("Please enter the first value: "))
numtwo = int(input ("Please enter the second value: "))

sum 
sum = numone + numtwo
print ("The sum is : ",sum)

# Question three :  Convert temperature from Celsius to Fahrenheit.

# Answer

# create two varibles call celsius(C) and Fahrenheit(F)
# Prompt the user to enter the celsius value
# Assign the known formula's to Fahrenheit (C/32 *47)
# Print the Fahrenheit variable .

C = 000
F = 0.00

C= float(input("Please enter the temperature (C'): "))
F = ((9/5)  * C) + 32.
print ("The temperature in Fahrenheit is : " , F)




# Practice Questions

# Write a Python program to calculate the area of a rectangle given its length and width

lenght = 0.00
width = 0.00
Area = 0.00
print("")
print("---PROGRAM TO CALCULATE AREA OF A RECTANGLE---")
lenght = float(input("Please enter the lenght: "))
width = float(input("Please enter the width: "))
Area = lenght * width

print (" The Area is : " , Area , "cm")

#Create a program that takes a user's name and age as input and prints a greeting message
username = ""
age = 0
print(''' 

Welcome to the Greatings Game

''')

username = input("Please enter your name: ")
age = int(input ("Please enter your age: "))
print ("Welcome once again ," , username)
print ("I heard a rumor of you been" , age , "years old")


# Write a program to check if a number is even or odd
print(''' 

Welcome to the even or odd number game

''')
picker = 0

picker = int(input("Please enter any whole number:  "))

if(picker % 2 == 0 ):
    print("The number your entered is an even number")
else:
    print("The number your entered is an odd number")
    