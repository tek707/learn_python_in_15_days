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


#Given a list of numbers, find the maximum and minimum values
list = [1,2,3,4,5,6,7]

max = 0
min = 100

for i in list:
    if(i > max):
        max = i
    else:
        max = max
    if(i < min):
        min = i
    else:
        min = min
print("The max is : " , max)
print("The min is : " , min)

#Create a Python function to check if a given string is a palindrome 
print(''' 

Welcome to the palindrome

''')

def palindrome(s):
    return s == "".join(reversed(s))

usertext = input("Please enter a word: ")
result = palindrome(usertext)
print("Is it a palindrome?", result) 


#Calculate the compound interest for a given principal amount, interest rate, and time period
print(''' 

Welcome to the simple intrest calculated

''')
Principal = int(input("Please enter your principal amount: "))
Rate = float(input("Please enter your rate % value: "))
Time =int( input("Please enter your time: "))
#simple intrest as SI
SI = 0.00
SI = (Principal *( Rate *0.01)*Time )/100
print("Your simple intrest is: " , SI)


#Write a program that converts a given number of days into years, weeks, and days
print(''' 

Welcome to the full year calculator

''')
Edays = int(input("Please enter the number of days:  "))

days = Edays
weeks = int(days / 7)
months =int( weeks / 4)
years = int(months / 52)

print(" You have: Years: " , years , "months: " , months ,"weeks", weeks ,  "Days: " , days)


#Given a list of integers, find the sum of all positive numbers
sumlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
newsum = 0
for i in sumlist:
    if(i%2==0):
        newsum+=i
print("Sum of all the even numbers is: ",newsum)


#Create a program that takes a sentence as input and counts the number of words in it
def count_words(sentence):
    words = sentence.split()
    return len(words)

user_input = input("Enter a sentence: ")
result = count_words(user_input)
print("Number of words:", result)



