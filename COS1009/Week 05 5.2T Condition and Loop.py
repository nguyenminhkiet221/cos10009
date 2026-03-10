#ALGORITHM WORKBENCH
#1  Write an if statement that assigns 20 to the variable y, and assigns 40 to the variable z if the variable x is greater than 100.

import turtle


x = int(input("Enter the number for x: "))
if x > 100:
    y = 20
    z = 40
    print("y =", y)
    print("z =", z)

#2 Write an if statement that assigns 10 to the variable b and 50 to the variable c if the variable a is equal to 100. 

a = int(input("Enter the number for a:"))
if a == 100:
    b = 10
    c = 50
    print("b=" , b)
    print("c=" , c)

#3  Write an if-else statement that assigns 0 to the variable b if the variable a is less than 10. 
#   Otherwise, it should assign 99 to the variable b.

a = int(input("Enter the number for a:"))
if a < 10:
    b = 0
else:
    b =99
print("b=" , b)

# 4  The following code contains several nested if-else statements. 
# Unfortunately, it was written without proper alignment and indentation. 
# Rewrite the code and use the proper conventions of alignment and indentation.

# if score >= A_score: 
# print('Your grade is A.') 
# else: 
# if score >= B_score: 
# print('Your grade is B.') 
# else: 
# if score >= C_score: 
# print('Your grade is C.') 
# else: 
# if score >= D_score: 
# print('Your grade is D.') 
# else: 
# print('Your grade is F.') 


if score >= A_score: 
    print('Your grade is A.') 
else: 
    if score >= B_score: 
        print('Your grade is B.') 
    else: 
        if score >= C_score: 
            print('Your grade is C.') 
        else: 
            if score >= D_score: 
                print('Your grade is D.') 
            else: 
                print('Your grade is F.') 

#5 Write nested decision structures that perform the following: If amount1 is greater than 10 and 
# amount2 is less than 100, display the greater of amount1 and amount2.

amount1 = int(input("Enter amount1: "))
amount2 = int(input("Enter amount2: "))
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print("Greater amount is:", amount1)
    else:
        print("Greater amount is:", amount2)
        

# 6. Write an if-else statement that assigns True to the again variable if the score variable is within 
# the range of 40 to 49. If the score variable’s value is outside this range, assign False to the again 
# variable. 

score = int(input("Enter the score: "))
if 40 <= score <= 49:
    again = True
else:
    again = False
print("again =", again)

# 7. Write an if-else statement that determines whether the points variable is outside the range of 9 
# to 51. If the variable’s value is outside this range it should display “Invalid points.” Otherwise, it 
# should display “Valid points.”

points = int(input("Enter the points: "))
if points < 9 or points > 51:
    print("Invalid points.")        
else:
    print("Valid points.")  

# 8. Write an if statement that uses the turtle graphics library to determine whether the turtle’s 
# heading is in the range of 0 degrees to 45 degrees (including 0 and 45 in the range). If so, raise 
# the turtle’s pen. 

import turtle
heading = turtle.heading()
if 0 <= heading <= 45:
    turtle.penup()
turtle.done()

# 9. Write an if statement that uses the turtle graphics library to determine whether the turtle’s pen 
# size is greater than 1 or the pen color is red. If so, set the pen size to 1 and the pen color to blue. 

import turtle
pensize = turtle.pensize()
pencolor = turtle.pencolor()
if pensize > 1 or pencolor == "red":
    turtle.pensize(1)
    turtle.pencolor("blue")
turtle.done()

# 10. Write an if statement that uses the turtle graphics library to determine whether the turtle is 
# inside of a rectangle. The rectangle’s upper-left corner is at (100, 100) and its lower-right corner 
# is at (200, 200). If the turtle is inside the rectangle, hide the turtle. 


import turtle
x = turtle.xcor()
y = turtle.ycor()
if 100 < x < 200 and 100 < y < 200:
    turtle.hideturtle()
turtle.done()

#================================================================================================================================================================================
#LOOP

# 1. Write a while loop that lets the user enter a number. The number should be multiplied by 10, 
# and the result assigned to a variable named product. The loop should iterate as long as product is 
# less than 100. 

number = int(input("Enter a number: "))
product = number * 10
while product < 100:
    print("Product is:", product)
    number = int(input("Enter a number: "))
    product = number * 10

# 2. Write a while loop that asks the user to enter two numbers. The numbers should be added and 
# the sum displayed. The loop should ask the user if he or she wishes to perform the operation 
# again. If so, the loop should repeat, otherwise it should terminate.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print("The sum is:", sum)
again = input("Do you want to perform the operation again? (yes/no): ")

while again == "yes":
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    sum = number1 + number2
    print("The sum is:", sum)
    again = input("Do you want to perform the operation again? (yes/no): ")
    
# 3. Write a for loop that uses the range function to display all odd numbers between 1 and 100. 

for i in range(1, 101, 2):
    print(i)

# 4. Starting with a variable text containing an empty string, write a loop that prompts the user to 
# type a word. Add the user’s input to the end of text and then print the variable. The loop should 
# repeat while the length of text is less than 10 characters. 

text = ""
while len(text) < 10:
    word = input("Type a word: ")
    text += word
    print(text)

# 5. Write a loop that calculates the total of the following series of numbers: 
# [ 
#  {1}/{30} + {2}/{29} + {3}/{28} + ….. + {30}/{1} 
# ] 

total = 0.0
for i in range(1,31):
    total += i/(31-i)
print("The total is:", total)