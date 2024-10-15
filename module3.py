# Ulugbek Medetov
# 11.14.2024

# # Program prints Hello World
print("Hello World")

# # Asks a user their name and greets them by their name.
name = input("What is your name? ")
print("Hello", name)

# # Calculates the area of a circle
radius = float(input("Input the radius: "))
area = radius**2*3.14
print("The area of square is: ", area)

# # Calculates MPG of a car
miles = float(input("Miles travelled = "))
gallons = float(input("Gallons used = "))
mpg = miles/gallons
print("The car's MPG is ", mpg)

# # Converts Fahrenheit to Celcius
f = float(input("Input degrees in Fahrenheit: "))
c = (f-32)*5/9
print(f, "Fahrenheit equals to", c, "in Celcius")

# Finds on which day of the week you will come back from vacation
def find_end_day(starting_day, number_of_days):
    return_day = (starting_day + number_of_days) % 7
    return return_day

starting_day = int(input("Please input the starting day in numbers(Note: 1-Monday, 7-Sunday): "))
number_of_days = int(input("Please input the number of days you are going to rest: "))

return_day = find_end_day(starting_day, number_of_days)

print(f"You will be back on day number: {return_day}")    

# Finds leap yeards between 1900 and 2100
def extra_credit_problem_1():
    start_year = 1900
    end_year = 2100
    # TODO: Write a program to print leap years from the year 1900 to 2100
    # 5 points extra credits
    for years in range(1900, 2100):
        if years % 4 == 0:
            print(years)
extra_credit_problem_1()

# Checks if the given number is prime number or not
n = int(input("Input an integer number to check if it is prime number or not: "))
def extra_credit_problem_2(n):
    # a prime number is a natural number greater than 1, that can only divisible by itself and 1
    # 10 points extra credits
    # TODO: given the number n, check if n is a prime number
    if n > 2:
        for numbers in range(2, n):
            if n % numbers == 0:
                print(f"{n} is not a prime number")
            else:
                print(f"{n} is a prime number")
    elif n == 2:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
extra_credit_problem_2(n)

# Sorry I did not see the document at first. So i just wrote all the codes on a blank file i created.
# I saw the document only after i completed 7 assignments and searched for additional credit ones.


    


