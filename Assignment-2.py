# 1. Calculate Profit Percentage

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100

    print("Profit:", profit)
    print("Profit Percentage:", round(profit_percentage, 2), "%")

elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100

    print("Loss:", loss)
    print("Loss Percentage:", round(loss_percentage, 2), "%")

else:
    print("No Profit No Loss")

# 2. Cricket Stats Analyzer

p1 = int(input("Enter runs scored by Player 1: "))
p2 = int(input("Enter runs scored by Player 2: "))
p3 = int(input("Enter runs scored by Player 3: "))
p4 = int(input("Enter runs scored by Player 4: "))
p5 = int(input("Enter runs scored by Player 5: "))

total_runs = p1 + p2 + p3 + p4 + p5
average_runs = total_runs / 5

print("Total Runs:", total_runs)
print("Average Runs:", average_runs)

# 3. Retirement Age Calculator

age = int(input("Enter your age: "))

if age < 65:
    years_left = 65 - age
    print("Years left until retirement:", years_left)
else:
    print("You have already reached retirement age.")

# 4. Area of Circle

import math

radius = float(input("Enter radius: "))

area = math.pi * radius ** 2

print("Area of Circle:", round(area, 2))

# 5. Salary Calculation

base_salary = 50000
bonus = 5000
tax_rate = 10 / 100
other_charges = 2000

gross_salary = base_salary + bonus
tax = gross_salary * tax_rate
net_salary = gross_salary - tax - other_charges

print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary)

# 6. Bank Loan Approval System

age = int(input("Enter Age: "))
income = float(input("Enter Monthly Income: "))
credit_score = int(input("Enter Credit Score: "))
debt = float(input("Enter Outstanding Debt: "))

if age >= 18 and age <= 60 and income >= 25000 and credit_score >= 700 and debt <= 10000:
    print("Loan Approved")
else:
    print("Loan Rejected")

# 7. Student Interview Eligibility Checker

academic_score = float(input("Enter Academic Score: "))
attendance = float(input("Enter Attendance Percentage: "))
activity = input("Participated in Extracurricular Activities (yes/no): ")

if academic_score >= 60 and attendance >= 75 and activity.lower() == "yes":
    print("Eligible for Interview")
else:
    print("Not Eligible for Interview")

# 8. Email Domain Validation

email = input("Enter Email Address: ")

if "gmail.com" in email:
    print("Eligible for Registration")
else:
    print("Not Eligible for Registration")

# 10. Student Grading System

marks = float(input("Enter Marks: "))

if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks <= 89:
    print("Grade B")
elif 70 <= marks <= 79:
    print("Grade C")
elif 60 <= marks <= 69:
    print("Grade D")
elif 50 <= marks <= 59:
    print("Grade E")
elif 0 <= marks <= 49:
    print("Grade F")
else:
    print("Invalid Marks")

# 11. Authentication System

valid_username = "user1"
valid_password = "pass@123"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == valid_username and password == valid_password:
    print("Authentication Successful")
else:
    print("Authentication Failed")

# 12. Employee Salary Based on Experience

experience = int(input("Enter Years of Experience: "))

if experience >= 10:
    salary = 80000
    print("Senior Employee")

    if experience > 15:
        salary += 5000
        print("Experience exceeds 15 years. Bonus added.")

elif experience >= 5:
    salary = 50000
    print("Mid-Level Employee")

else:
    salary = 30000
    print("Junior Employee")

print("Salary:", salary)

# 13. Library Charge Calculation

days = int(input("Enter Number of Days: "))

if days <= 5:
    charge = days * 2
elif days <= 10:
    charge = days * 3
elif days <= 15:
    charge = days * 4
else:
    charge = days * 5

print("Library Charge: ₹", charge)

# 14. Arrange Three Numbers in Descending Order

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

numbers = [num1, num2, num3]
numbers.sort(reverse=True)

print("Numbers in Descending Order:", numbers)

# 15. Tax Calculation for Car Purchase

brand = input("Enter Car Brand: ").lower()
price = float(input("Enter Car Price: "))

tax = 0

if brand == "mahindra" and 700000 <= price <= 1000000:
    tax = price * 0.05

elif brand == "audi" and 1000000 <= price <= 1500000:
    tax = price * 0.10

elif brand == "jaguar" and 1500000 <= price <= 2000000:
    tax = price * 0.25

elif brand == "mercedes" and 2000000 <= price <= 2500000:
    tax = price * 0.30

else:
    print("No Tax Rule Available")

print("Tax Amount:", tax)

# 16. Finding the Middle Number

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

numbers = [a, b, c]
numbers.sort()

print("Middle Number:", numbers[1])

# 17. Find Greatest Number

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

greatest = max(a, b, c)

print("Greatest Number:", greatest)

# 18. Authentication System

username = "user1"
password = "pass@123"

u = input("Enter Username: ")
p = input("Enter Password: ")

if u == username and p == password:
    print("Authentication Successful")
else:
    print("Authentication Failed")

# 19. Class Attendance Percentage

total_classes = int(input("Enter Total Classes Held: "))
attended_classes = int(input("Enter Classes Attended: "))

attendance_percentage = (attended_classes / total_classes) * 100

print("Attendance Percentage:", round(attendance_percentage, 2), "%")

if attendance_percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

#20. Library Charge Calculation

days = int(input("Enter Number of Days: "))

if days <= 5:
    amount = days * 2

elif days <= 10:
    amount = days * 3

elif days <= 15:
    amount = days * 4

else:
    amount = days * 5

print("Total Charge: ₹", amount)

# 21. UPSC Selection Process

age = int(input("Enter Age: "))
graduate = input("Graduate (yes/no): ")
nationality = input("Nationality: ")

if 21 <= age <= 32 and graduate.lower() == "yes" and nationality.lower() == "indian":

    print("Eligible for UPSC")

    prelims = int(input("Enter Prelims Score: "))
    prelim_cutoff = 100

    if prelims >= prelim_cutoff:

        mains = int(input("Enter Mains Score: "))
        mains_cutoff = 200

        if mains >= mains_cutoff:

            interview = int(input("Enter Interview Score: "))
            interview_cutoff = 75

            if interview >= interview_cutoff:
                print("Congratulations! You have cleared UPSC.")
            else:
                print("You failed the Interview.")

        else:
            print("You failed the Mains.")

    else:
        print("You failed the Prelims.")

else:
    print("Not Eligible for UPSC")

#22. Menu Driven Login System

print("1. Login with Phone")
print("2. Login with Email")
print("3. Exit")

choice = int(input("Enter Choice: "))

phone = "1234567890"
otp = "1234"

email = "user@example.com"
password = "password123"

if choice == 1:

    p = input("Enter Phone Number: ")
    o = input("Enter OTP: ")

    if p == phone and o == otp:
        print("Login Successful with Phone!")
    else:
        print("Invalid Phone Number or OTP")

elif choice == 2:

    e = input("Enter Email: ")
    pwd = input("Enter Password: ")

    if e == email and pwd == password:
        print("Login Successful with Email!")
    else:
        print("Invalid Email or Password")

elif choice == 3:
    print("Exiting Program. Have a Nice Day!")

else:
    print("Invalid Choice")

#23. KBC Quiz Game

start = input("Do you want to start the game? (yes/no): ")

if start.lower() == "yes":

    score = 0
    correct = 0
    wrong = 0
    skipped = 0

    questions = [
        ("Capital of India?", "A", ["A.Delhi", "B.Mumbai", "C.Kolkata", "D.Chennai"], 1000),
        ("2 + 2 = ?", "B", ["A.3", "B.4", "C.5", "D.6"], 2000),
        ("National Animal of India?", "C", ["A.Lion", "B.Elephant", "C.Tiger", "D.Deer"], 3000),
        ("Python is?", "D", ["A.OS", "B.Game", "C.Browser", "D.Programming Language"], 5000),
        ("Sun rises in?", "A", ["A.East", "B.West", "C.North", "D.South"], 10000)
    ]

    for question, answer, options, points in questions:

        print("\n", question)

        for option in options:
            print(option)

        user_answer = input("Enter Option (A/B/C/D) or Skip: ")

        if user_answer.lower() == "skip":
            skipped += 1

        elif user_answer.upper() == answer:
            print("Correct Answer")
            score += points
            correct += 1

        else:
            print("Wrong Answer")
            wrong += 1

    print("\n===== GAME OVER =====")
    print("Total Score:", score)
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Skipped Questions:", skipped)

else:
    print("Game Not Started")

