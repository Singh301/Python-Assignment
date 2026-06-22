# 1. Switch values of two integers

# Assign values
n1 = 20
n2 = 30

# Swap values
n1, n2 = n2, n1

print("n1 =", n1)
print("n2 =", n2)

# 2. Switch values of two strings

char1 = "hello"
char2 = "java"

# Swap string values
char1, char2 = char2, char1

print("char1 =", char1)
print("char2 =", char2)

# 3. Switch one string value with one integer value

n1 = 200
char2 = "java"

# Swap values
n1, char2 = char2, n1

print("n1 =", n1)
print("char2 =", char2)

# 5. Update balance after deposit

current_balance = 10000
deposit_balance = 5000

print("Before Deposit:", current_balance)

# Add deposit amount
current_balance += deposit_balance

print("After Deposit:", current_balance)

# 6. Update balance after withdrawal

balance = 12000
withdrawal = 3000

# Subtract withdrawal amount
balance -= withdrawal

print("Balance after withdrawal =", balance)

# 7. Increase shopping cart items by 3

cart_items = 5

# Increase by 3
cart_items += 3

print("Cart Items =", cart_items)

# 8. Apply a 20% discount

price = 1000

# Calculate discount
discount = price * 20 / 100

# Final price
price -= discount

print("Price after discount =", price)

# 9. Student Percentage

obtain_marks = 430
out_of = 500

percentage = (obtain_marks / out_of) * 100

print("Percentage =", percentage)

# 10. Total and Average of 4 Subjects

sub1 = 80
sub2 = 75
sub3 = 90
sub4 = 85

total = sub1 + sub2 + sub3 + sub4
average = total / 4

print("Total =", total)
print("Average =", average)

# 11. Average of 3 Numbers

num1 = 25
num2 = 35
num3 = 45

average = (num1 + num2 + num3) / 3

print("Average =", average)

# 12. Profit Percentage

cost_price = 500
selling_price = 600

profit = selling_price - cost_price
profit_percentage = (profit / cost_price) * 100

print("Profit Percentage =", profit_percentage)

# 13. Simple Interest

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

# 14. Compound Interest

principal = 10000
rate = 5
time = 2

amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)


# 15. Tax on Income

income = 500000
tax_rate = 10

tax = (income * tax_rate) / 100

print("Tax =", tax)

# 16. Percentage Increase

initial_value = 200
final_value = 250

percentage_change = ((final_value - initial_value) / initial_value) * 100

print("Percentage Change =", percentage_change)

# 17. Boolean to Integer

value = True

result = int(value)

print(result)

# 18. Float to String

num = 45.67

result = str(num)

print(result)
print(type(result))


# 19. Celsius to Fahrenheit

celsius = 20

fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit =", fahrenheit)


# 20. Fahrenheit to Celsius

fahrenheit = 50

celsius = (fahrenheit - 32) * 5/9

print("Celsius =", celsius)


# 21. Integer to Binary

num = 25

binary_value = bin(num)

print(binary_value)

# 22. Area of Triangle

base = 10
height = 6

area = 0.5 * base * height

print("Area =", area)


# 23. Perimeter of Square

side = 9

perimeter = 4 * side

print("Perimeter =", perimeter)


# 24. Diameter of Circle

radius = 14

diameter = 2 * radius

print("Diameter =", diameter)

# 25. Volume of Cube

side = 5

volume = side ** 3

print("Volume =", volume)

# 26. Surface Area of Cuboid

l = 4
b = 3
h = 2

surface_area = 2 * (l*b + b*h + l*h)

print("Surface Area =", surface_area)

# 27. Square of Sum (x+y)²

x = 5
y = 7

result = (x + y) ** 2

print(result)

# 28. x² - 4x + 4

x = 3

result = x**2 - 4*x + 4

print(result)

# 29. (a+b)(a-b)

a = 6
b = 2

result = (a + b) * (a - b)

print(result)

# 30. a³ + b³

a = 1
b = 2

result = a**3 + b**3

print(result)


# 31. (x-y)²

x = 10
y = 6

result = (x - y) ** 2

print(result)

# 32. x³ - y³

x = 4
y = 1

result = x**3 - y**3

print(result)

# 33. User Details Story

name = input("Enter Name: ")
age = input("Enter Age: ")
city = input("Enter City: ")
hobby = input("Enter Hobby: ")

print(f"Meet {name}, a {age}-year-old enthusiast from {city}.")
print(f"When not busy with daily tasks, {name} loves spending time {hobby}.")
print(f"Life in {city} keeps {name} energetic and curious every single day.")
print(f"With coding as a passion, the future looks creative and inspiring for {name} in the {city} City.")

# 34. Professional Profile

full_name = input("Enter Full Name: ")
profession = input("Enter Profession: ")
quote = input("Enter Favorite Quote: ")
experience = input("Enter Years of Experience: ")

print("-" * 50)
print("Name :", full_name)
print("Profession :", profession)
print("Experience :", experience, "years")
print(f'Quote : "{quote}"')
print("-" * 50)


# 35. Movie Ticket

movie_name = input("Enter Movie Name: ")
viewer_name = input("Enter Viewer Name: ")
seat_number = input("Enter Seat Number: ")
show_time = input("Enter Show Time: ")

print("\n Movie Ticket")
print("-" * 25)
print("Movie :", movie_name)
print("Name :", viewer_name)
print("Seat No :", seat_number)
print("Time :", show_time)
print("Enjoy the show!")
print("-" * 25)
