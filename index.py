# easy type in loops
# 1.. Print all numbers from 1 to 100 using a for loop.
for i in range(1, 101):
    print(i)

# 2.Write a program to print the sum of the first n natural numbers (Formula: n*(n+1)/2).

n = int(input("Enter a number: "))
sum_of_n = n * (n + 1) // 2
print(sum_of_n)


# 3. Print all even numbers between 1 and 50 using a while loop.

i = 2
while i <= 50:
    print(i)
    i += 2

# 4.Write a program to display the multiplication table of a given number 

num = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 21):
    print(f"{num} x {i} = {num * i}")


# 5.Reverse a number using a while loop and also sum the digits of the number.

number = int(input("Enter a number to reverse: "))
reverse = 0
sum_of_digits = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    sum_of_digits += digit
    number //= 10
print(f"The reversed number is: {reverse}")
print(f"The sum of digits is: {sum_of_digits}")


# 6.Write a program to count the number of digits in a given number using a while loop.

number = int(input("Enter a number to count its digits: "))
count = 0
while number > 0:
    count += 1
    number //= 10
print(f"The number of digits is: {count}")


# 7.Write a program that keeps asking the user to enter numbers until they enter a negative number using a while loop.

while True:
    number = int(input("Enter a number (negative number to stop): "))
    if number < 0:
        print("Negative number entered, exiting.")
        break
    else:
        print(f"You entered: {number}")


# medium questions

# 1. Print the first 10 terms of the Fibonacci series using a for loop.

n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 2. Check if a given number is a prime number using a for loop.

number = int(input("Enter a number to check if it's prime: "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


# 3.Write a program to calculate the factorial of a number using a while loop.

number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is: {factorial}")

# 4.Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")


# 5.Implement a menu-driven program where the user can choose to:
# 1.Find the square of a number.
# 2.Find the cube of a number.
# 3.Exit.

while True:
    print("\nMenu:")
    print("1. Find the square of a number")
    print("2. Find the cube of a number")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = float(input("Enter a number: "))
        print(f"The square of {num} is: {num ** 2}")
    elif choice == 2:
        num = float(input("Enter a number: "))
        print(f"The cube of {num} is: {num ** 3}")
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")



# 6.Implement a basic login system where the user has three attempts to enter the correct password using a loop.

correct_password = "143"
attempts = 3

while attempts > 0:
    entered_password = input("Enter your password: ")
    if entered_password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
        
    if attempts == 0:
        print("You have been locked out due to too many incorrect attempts.")













