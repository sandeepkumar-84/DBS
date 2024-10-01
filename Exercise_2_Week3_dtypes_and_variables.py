#Module Code: B9DA108 | Module Title: Programming for Data Analysis | School: DBS 
#Lecturer Name: Alexander Victor
#Exercise 2: Week3: Data Types and Variables to be completed by date:Monday, 7 October 2024, 5:02 PM
#Student Name: Sandeep Kumar | Student ID: 20049275 | Email: 20049275@mydbs.ie | Git: https://github.com/sandeepkumar-84/DBS.git
#1. Create a variable age and assign it the value 25.
print(f"1. Create a variable age and assign it the value 25.")

age = 25

print(f"   Varable age is assigned a value of {age}")

#2. Create a variable name and assign it a string containing your name.
print(f"2. Create a variable name and assign it a string containing your name.")

name = "Sandeep Kumar"

print(f"   Varable name is assigned a value of {name}")

#3. Print the type of the variable age.
print(f"3. Print the type of the variable age.")

print(f"   Type of variable age is  {type(age)}")

#4. Convert the variable age to a string and store it in a new variable age_str.
print(f"4. Convert the variable age to a string and store it in a new variable age_str.")

var_str_age = str(age)

print(f"   int variable age is conveted into string. value is  {var_str_age} and type is {type(var_str_age)}")

#5. Create a variable height and assign it the value 175.5 (floating-point number)
print(f"5. Create a variable height and assign it the value 175.5 (floating-point number)")

height = 175.5

print(f"   Float Varable height is assigned a value of {height}")

#6. Print the type of the variable height.
print(f"6. Print the type of the variable height.")

print(f"   Type of variable height is  {type(height)}")

#7. Create a variable is_student and assign it a boolean value representing whether you are a student or not.
print(f"7. Create a variable is_student and assign it a boolean value representing whether you are a student or not.")

is_student = True

if is_student == True:
    print(f"   I am a student as the value of var var_is_student has value {is_student} ")

#8. Print the type of the variable is_student.
print(f"8. Print the type of the variable is_student.")

print(f"   Type of variable is_student is  {type(is_student)}")

#9. Create a list colors containing the names of three colors.
print(f"9. Create a list colors containing the names of three colors.")

colors = ["Red","Blue","Green"]

print(f"    The list colors has following colors {colors}")

#10. Print the second element of the list colors.
print(f"10. Print the second element of the list colors.")

print(f"    The Second element of the list colors is {colors[1]}")

#11. Create a tuple dimensions containing the length, width, and height of a box.
print(f"11. Create a tuple dimensions containing the length, width, and height of a box.")

dimensions = (10,5,2)

print(f"    The dimension of the box is length {dimensions[0]} width {dimensions[1]} height {dimensions[2]}")

#12. Print the third element of the tuple dimensions.
print(f"12. Print the third element of the tuple dimensions.")

print(f"    The third element of the dimension tuple is  {dimensions[2]}")

#13. Create a dictionary person with keys ""name"", ""age"", and ""city"", and assign appropriate values.
print(f"13. Create a dictionary person with keys ""name"", ""age"", and ""city"", and assign appropriate values.")

person = {"name":"Jhon", "age":30,"city":"Dublin"}
print(f"    The person dictionary is assigned with values  {person}")


#14. Print the value associated with the key ""age"" in the dictionary person.
print(f"14. Print the value associated with the key ""age"" in the dictionary person.")

print(f"    The value of key age in person dictionary is {person["age"]}")

#15. Create a set unique_numbers containing three unique integers.
print(f"15. Create a set unique_numbers containing three unique integers.")

unique_numbers = {20,30,40}

print(f"    The unique_numbers containing three unique integers is created {unique_numbers}")

#16. Add a new integer to the set unique_numbers.
print(f"16. Add a new integer to the set unique_numbers.")

unique_numbers.add(10)

print(f"    unique_numbers is added with a new number and new set now looks like {unique_numbers}")

#17. Create a variable x and assign it the value 10.
print(f"17. Create a variable x and assign it the value 10.")

x = 10

print(f"17. Created a variable x and assigned it the value  {x}")

#18. Increment the value of x by 5.
print(f"18. Increment the value of x by 5.")

x = x + 5

print(f"17. Incremented variable x with value 5. x now has value {x}")

#19. Create a variable y and assign it the value of x squared.
print(f"19. Create a variable y and assign it the value of x squared.")

y = x**2

print(f"17. variable y is created and assigned a value of square of x. y now has value {y}")

#20. Swap the values of variables x and y.
print(f"20. Swap the values of variables x and y.")

#temporarily storing the value of x in a new variable. Then x is assigned with value of y and finally y is assigned with the value stored in the temp variable

print(f"The original value of x and y were : x = {x} and y = {y}")

var_temp = x
x = y
y = var_temp

print(f"After swapping their values are:x = {x} and y = {y} ")