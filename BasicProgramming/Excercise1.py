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
print(f"4 is {check_odd_or_even(4)} number")


    






