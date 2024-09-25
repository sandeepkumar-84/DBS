#Module Code: B9DA108 | Module Title: Programming for Data Analysis | School: DBS 
#Lecturer Name: Alexander Victor
#Exercise 1: Week2: Python Basics To be completed by date:Tuesday, 1 October 2024, 11:00 AM
#Student Name: Sandeep Kumar | Student ID: 20049275 | Email: 20049275@mydbs.ie | Git: https://github.com/sandeepkumar-84/DBS.git

#Importing time, random and match libraries to be used in the code. 

import time
import random
import math

#1. Write a program that prints "Hello, World!" to the console

print("1. Write a program that prints \"Hello, World!\" to the console")
print("   Hello, World!\n")


#2 Calculate the area of a rectangle given its length and width.
print("2. Calculate the area of a rectangle given its length and width.")
      
width = 10
length = 25
print(f"   Area of a rectangle with width:{width} and length {length} is {width*length}\n")

#3 Convert temperature from Celsius to Fahrenheit and vice versa.

print("3. Convert temperature from Celsius to Fahrenheit and vice versa.")

temp_in_celsius = 24
temp_in_farenheight = (temp_in_celsius * 9/5) + 32

print(f"   {temp_in_celsius} in celcius is equal to  {temp_in_farenheight} in Farenheight")

temp_in_celsius = (temp_in_farenheight-32) * 5/9

print(f"   {temp_in_farenheight} in Farenheight is equal to  {temp_in_celsius} in Celsius \n")

#4. Create a list of numbers and print the sum of all the elements.
print("4. Create a list of numbers and print the sum of all the elements.")

list_numbers = [1,3,5,7,9,11,13]
sum = 0
for num in list_numbers:
    sum = sum + num
print(f"   Sum of the numbers in the list {list_numbers} is {sum}\n")

#5. Write a program to check if a given number is even or odd.
print("5. Write a program to check if a given number is even or odd.")
def check_odd_or_even(num_to_be_checked):
    if(num_to_be_checked % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(f"   5 is {check_odd_or_even(5)} number")
print(f"   4 is {check_odd_or_even(4)} number\n")

#6. Generate a random number between 1 and 100 and ask the user to guess it.
print("6. Generate a random number between 1 and 100 and ask the user to guess it.")
sys_random_num = random.randrange(1,100)
user_rand_num = input("   System has generated a random number. Can you guess it?")

if(sys_random_num == user_rand_num):
    print("Your guess {user_rand_num} is correct\n")
else:
    print(f"   Your guess {user_rand_num} is incorrect as system generated random number was {sys_random_num}\n")

# Sleep/delay is added so that user can check the result and then other code is executed
time.sleep(2)
#7. Write a function to check if a given string is a palindrome.
print("7. Write a function to check if a given string is a palindrome.")

# Characters are compared from start and end of the list of the input string. loop executes till the middle of it. 
#is_palindrome is true until characters are found different breaking the loop. 
def check_palindrome(word):
        length_word = len(word)
        start = 0
        is_palindrome = True
        list_alph = []
        for w in word.lower():
            list_alph.append(w)       
        
        while(start < math.floor(length_word/2)):             
             if(list_alph[start] == list_alph[length_word-(start+1)]):                  
                  start  = start + 1                  
             else:
                 is_palindrome = False
                 break
             
             
        return is_palindrome


def diplay_palidrome_results(word):
    if (check_palindrome(word)):
        print(f"   Word {word} is a palidrome.\n")
    else: 
        print(f"   Word {word} is not a palidrome.\n")

diplay_palidrome_results("Madam")
diplay_palidrome_results("Palindrome")
diplay_palidrome_results("Noon")

#8. Calculate the factorial of a given number.
print("8. Calculate the factorial of a given number.")

# Recursive approach is used till number is reduced to 1 or 0. 

def find_factorial(num):
    if(num ==0 or num == 1):
        return 1
    else:
        return num * (num -1)
print(f"   The factorial of number 5 is {find_factorial(5)}\n")

#9. Write a program to find the largest element in a list.
print("9. Write a program to find the largest element in a list.")

max_num  = max(list_numbers)
print(f"   Largest number in the list {list_numbers} is {max_num}\n")

#10 Create a simple calculator that can perform addition, subtraction, multiplication, and division.
print("10 Create a simple calculator that can perform addition, subtraction, multiplication, and division.")
def calculator_simulator(a,b,operation):
    match operation:
        case "Addition":        
            return a + b
        case "1":
            return a + b
        case "Substraction":
            return a - b
        case "2":
            return a - b
        case "Multiplication":
            return a * b
        case "3": 
            return a * b
        case "Division":
            if b != 0:
                return a / b
            else:
                return "Bad Request"
        case "4":
            if b != 0:
                return a / b
            else:
                return "Bad Request"
        case _: 
            return "Bad Redquest"

first_number = int(input("Please provide first number = "))
second_number = int(input("Please provide second number = "));
operation = input("Please provide operation by either selecting serial number or operation from 1. Addition 2. Substraction 3. Multiplication 4. Division = ");

print(f"Result of the above calculation is {calculator_simulator(first_number, second_number, operation)}\n")
# Sleep/delay is added so that user can check the result and then other code is executed
time.sleep(2)

#11. Write a function to find the square root of a number using Newton's method.
print("11. Write a function to find the square root of a number using Newton's method.")

# Newtons formula for iterations is defined in a function
def sql_root_iteration(xn,num):
    xnp1 = (xn + (num/xn))/2
    return xnp1

# Newtons iteration function is called using this function. Guess is assumed to be input number by 2.
# Range  is hard coded to 16 for large values 
def cal_newton_root(num):
  listIterations = []
  guess = num/2
  for i in range(16):
    guess = sql_root_iteration(guess,num)
    listIterations.append(guess)
  return listIterations[len(listIterations)-1]

print(f"    Square root of 3 is {cal_newton_root(3)}")
print(f"    Square root of 64 is {cal_newton_root(64)}")
print(f"    Square root of 625 is {cal_newton_root(625)}\n")

#12 Reverse a given list without using the reverse() method.
print("12. Reverse a given list without using the reverse method.")

def rev_givent_str(inputList):
    length = len(inputList)
    rev_list_str = []
    row = 0
    while(row < length):
        rev_list_str.append(inputList[length-(row + 1)])
        row = row + 1
    return rev_list_str

list_str = ["1","2","3","4","5"]

print(f"   The reverse of the list {list_str} is {rev_givent_str(list_str)}\n")

#13. Write a program to find all the prime numbers between 1 and 100.
print("13. Write a program to find all the prime numbers between 1 and 100.")

# Loop starts from 4 as 2 and 3 are Natural primes, untill it reaches the 100 
# Inner loop checks the divisibilty from 2 till the number itself. If anytime a divisor is found loop exits 
# else if no divisor is found then prime number is appended to the list.    
def find_prime_lt(num):
    checkNum =  4
    list_prime = []
    list_prime.append(2)
    list_prime.append(3)
    while(checkNum <= num):
        x = 2
        is_prime = True
        while(x < checkNum):
            if(checkNum % x == 0):
                is_prime = False
                break
            else: 
                x = x + 1
        if(is_prime):
            list_prime.append(checkNum)
        checkNum = checkNum + 1
    return list_prime

print(f"   List of prime numbers less than 100 is {find_prime_lt(100)}\n")

#14. Calculate the Fibonacci sequence up to a given number.
print(f"14. Calculate the Fibonacci sequence up to a given number.")

# recursive approach is used in function to find the nth fibonacci. 
def find_fibonacci(num):
    if num == 1:
        
        return 1
    elif num <= 0:
        
        return 0
    else:
        
        return find_fibonacci(num - 1) + find_fibonacci(num - 2)

# function prints all the n fibonacci numbers until it is less than given input (sum ) 
def find_fibonacdi_lt(sum):
    less_than = 1
    while find_fibonacci(less_than) < sum:
        print(find_fibonacci(less_than))
        less_than = less_than + 1
    return ""

print(f"   Print all the find_fibonacci numbers less than 30")
find_fibonacdi_lt(30)
print("\n")

#15. Write a function to count the number of vowels in a given string.
print("15. Write a function to count the number of vowels in a given string.")

# vowels are predefined in a list and input is looped through and each alphabet is checked against the predefined list. 
def count_vowels(given_str):
    count = 0
    list_vowels = ['a','e','i','o','u']
    for x in given_str:
        if list_vowels.__contains__(x):
            count = count + 1
    return count

print(f"    The number of vowels in string {'experiment'} are {count_vowels('experiment')}")
print(f"    The number of vowels in string {'vowels'} are {count_vowels('vowels')}")
print(f"    The number of vowels in string {'rythm'} are {count_vowels('rythm')}\n")

#16 Check if a given year is a leap year.
print("16 Check if a given year is a leap year.")

def check_leap_year(input_year):
    if input_year % 4 == 0:
        return "leap year"
    else:
        return "non leap year"
    
print(f"   Year 2024 is  a {check_leap_year(2024)}")
print(f"   Year 2025 is  a {check_leap_year(2025)}\n")

#17. Remove duplicates from a list without using sets.
print("17. Remove duplicates from a list without using sets.")

# unique list is constructed in a loop by iterating through each character in the original string. 
# if the charatcter is already added, it will not be appended. 
def remove_duplicates(listOrig):
    listUniq = []
    for x in listOrig:
        if listUniq.__contains__(x) == False:
            listUniq.append(x)    
    return listUniq

listOrig = [1,2,3,3,4,5,5,7,7,7,7]
print(f"    Original list {listOrig}")
print(f"    List after removal of duplicates {remove_duplicates(listOrig)}\n")

#18. Write a program to sort a list of numbers using bubble sort.
print("18. Write a program to sort a list of numbers using bubble sort.")


def bubble_sort(listOrig):
    for x in range(0,len(listOrig)):
        for y in range(x+1,len(listOrig)-1):
            if listOrig[x] > listOrig[y]:
               z = listOrig[x]
               listOrig[x] = listOrig[y]
               listOrig[y] = z
    return listOrig
listOrig = [4,3,6,5,1,0,8]
print(f"    Original list {listOrig}")
print(f"    List after bubble sort  {bubble_sort(listOrig)}\n")


#19. Create a dictionary of names and ages, and print the name of the oldest person.
print("19. Create a dictionary of names and ages, and print the name of the oldest person.")
old_age = {"John":"58","Dow":"67","Paul":"60","Zen":"65"}
print(f"    The old age dictionary looks like {old_age}")

#items of the dictionary is queried for max age value
oldest_person = [name for name, age in old_age.items() if age == max(old_age.values())]
print(f"    The oldest person in the above dictionary is {str(oldest_person)[2:-2]}")

#20. Write a program to find the least common multiple (LCM) of two numbers.
print("20. Write a program to find the least common multiple (LCM) of two numbers.")

#basic approach of  is used
# lists for first input numbers is created, this will hold the multipliers of the num1 like num1*1, num1*2....
# lists for first input numbers is created, this will hold the multipliers of the num2 like num2*1, num2*2.... 
# inner for loop, loops through first list and check each item in list 2. If item is present then it is the lcm and loop breaks 
# outer while loop runs until lcm is found.  

def find_lcm(num1, num2):
    factorsNum1 = []
    factorsNum2 = []
    stop_loop = True
    multipleNum = 1
    lcm = 0
    while(stop_loop):
        factorsNum1.append(num1 * multipleNum)
        factorsNum2.append(num2 * multipleNum)
        for item in factorsNum1:
            if(factorsNum2.__contains__(item)):
                factorsNum1
                lcm = item
                stop_loop = False
                break
        multipleNum = multipleNum + 1
        
    return lcm

print(f"    LCM of numers 2,3 is {find_lcm(2,3)}")
print(f"    LCM of numers 10,15 is {find_lcm(10,15)}")

