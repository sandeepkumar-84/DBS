#Exercise 1: Week2: Python Basics To be completed by date:Tuesday, 1 October 2024, 11:00 AM

#1. Write a program that prints "Hello, World!" to the console

print("1. Write a program that prints \"Hello, World!\" to the console")
print("Hello, World!\n")


#2 Calculate the area of a rectangle given its length and width.
print("2. Calculate the area of a rectangle given its length and width.")
      
width = 10
length = 25
print(f"Area of a rectangle with width:{width} and length {length} is {width*length}\n")

#3 Convert temperature from Celsius to Fahrenheit and vice versa.

print("3. Convert temperature from Celsius to Fahrenheit and vice versa.")

temp_in_celsius = 24
temp_in_farenheight = (temp_in_celsius * 9/5) + 32

print(f" {temp_in_celsius} in celcius is equal to  {temp_in_farenheight} in Farenheight")

temp_in_celsius = (temp_in_farenheight-32) * 5/9

print(f" {temp_in_farenheight} in Farenheight is equal to  {temp_in_celsius} in Celsius \n")

#4. Create a list of numbers and print the sum of all the elements.
print("4. Create a list of numbers and print the sum of all the elements.")

list_numbers = [1,3,5,7,9,11,13]
sum = 0
for num in list_numbers:
    sum = sum + num
print(f"Sum of the numbers in the list {list_numbers} is {sum}\n")

#5. Write a program to check if a given number is even or odd.
print("5. Write a program to check if a given number is even or odd.")
def check_odd_or_even(num_to_be_checked):
    if(num_to_be_checked % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(f"5 is {check_odd_or_even(5)} number")
print(f"4 is {check_odd_or_even(4)} number\n")

#6. Generate a random number between 1 and 100 and ask the user to guess it.
print("6. Generate a random number between 1 and 100 and ask the user to guess it.")

import random
sys_random_num = random.randrange(1,100)
user_rand_num = input("System has generated a random number. Can you guess it?")

if(sys_random_num == user_rand_num):
    print("Your guess {user_rand_num} is correct\n")
else:
    print(f"Your guess {user_rand_num} is incorrect as system generated random number was {sys_random_num}\n")

#7. Write a function to check if a given string is a palindrome.
print("7. Write a function to check if a given string is a palindrome.")

import math
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
        print(f"Word {word} is a palidrome.\n")
    else: 
        print(f"Word {word} is not a palidrome.\n")

diplay_palidrome_results("Madam")
diplay_palidrome_results("Palindrome")
diplay_palidrome_results("Noon")

#8. Calculate the factorial of a given number.
print("8. Calculate the factorial of a given number.")

def find_factorial(num):
    if(num ==0 or num == 1):
        return 1
    else:
        return num * (num -1)
print(f"The factorial of number 5 is {find_factorial(5)}\n")

#9. Write a program to find the largest element in a list.
print("9. Write a program to find the largest element in a list.")

max_num  = max(list_numbers)
print(f"Largest number in the list {list_numbers} is {max_num}\n")

#10 Create a simple calculator that can perform addition, subtraction, multiplication, and
#division.

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

#11. Write a function to find the square root of a number using Newton's method.
print("11. Write a function to find the square root of a number using Newton's method.")
    
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

print(f"The reverse of the list {list_str} is {rev_givent_str(list_str)}\n")

#13. Write a program to find all the prime numbers between 1 and 100.
print("13. Write a program to find all the prime numbers between 1 and 100.")

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

print(f"List of prime numbers less than 100 is {find_prime_lt(100)}")

#14. Calculate the Fibonacci sequence up to a given number.
print(f"14. Calculate the Fibonacci sequence up to a given number.")

def find_fibonacci(num):
    if num == 1:
        
        return 1
    elif num <= 0:
        
        return 0
    else:
        
        return find_fibonacci(num - 1) + find_fibonacci(num - 2)


def find_fibonacdi_lt(sum):
    less_than = 1
    while find_fibonacci(less_than) < sum:
        print(find_fibonacci(less_than))
        less_than = less_than + 1
    return ""

print(f"Print all the find_fibonacci numbers less than 30")
find_fibonacdi_lt(30)





