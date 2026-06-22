# Q1. Print all Odd and Even Numbers from 1 to 20 .

# Print Even Numbers
print("Even Numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Print Odd Numbers
print("Odd Numbers:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
print("\n")

# Print multiples of 12 up to 120

for i in range(1, 11):
    print(12 * i)

# Q3. Generate Table of a Number

num = int(input("Enter a number: "))

print("Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Q4. Check Prime Number

num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# Q5. Sum Between Starting and Ending Point

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

total = 0

for i in range(start, end + 1):
    total += i

print("Sum =", total)

# Q6. Product Between Starting and Ending Point

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

product = 1

for i in range(start, end + 1):
    product *= i

print("Product =", product)

# Q7. Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("\n")

# Q8. Factorial of a Number

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

# Q9. Greatest Character from "python"

text = "python"

greatest = text[0]

for ch in text:
    if ch > greatest:
        greatest = ch

print("Greatest Character:", greatest)

# Q10. Display All Letters Except 'm' and 'i'

text = "Dreamer infotech"

for ch in text:
    if ch != 'm' and ch != 'i':
        print(ch, end="")


print("\n")

# Q11. Print Alternate Characters from a String

text = input("Enter a string: ")

# Print characters at even positions
for i in range(0, len(text), 2):
    print(text[i], end="")

print("\n")

# Q12. Reverse a String

text = input("Enter a string: ")

reverse = ""

# Traverse string from end to start
for i in range(len(text)-1, -1, -1):
    reverse += text[i]

print("Reversed String:", reverse)

print("\n")

# Q13. Count Total Characters in a String

text = input("Enter a string: ")

count = 0

for ch in text:
    count += 1

print("Total Characters:", count)

print("\n")

# Q14. Check Whether String is Palindrome

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

print("\n")

# Q15. Search a Character in a String

text = input("Enter a string: ")
search = input("Enter character to search: ")

found = False

for ch in text:
    if ch == search:
        found = True
        break

if found:
    print("Character Found")
else:
    print("Character Not Found")

print("\n")

# Q16. Filter Out Vowels and Consonants

text = input("Enter a string: ")

vowels = ""
consonants = ""

for ch in text:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        if ch in "AEIOUaeiou":
            vowels += ch
        else:
            consonants += ch

print("Vowels:", vowels)
print("Consonants:", consonants)

# Q17. Remove Duplicate Characters

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("After Removing Duplicates:", result)

# Q18. Display All Possible Pairs of 3

for i in range(1, 4):
    for j in range(1, 4):
        print(i, ":", j)


# Q19. Generate Pattern of Letter H

for i in range(7):
    
    if i == 3:
        print("* * * * *")
    else:
        print("*       *")

# Q20. Find Duplicate Letters Between Two Strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Common Characters:")

for ch in str1:
    if ch in str2:
        print(ch)

# Without Duplicate Printing
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = ""

for ch in str1:
    if ch in str2 and ch not in common:
        common += ch

print("Duplicate Letters:", common)

# Q21. Display Squares of Numbers from 1 to 10

for i in range(1, 11):
    print(i, "=", i * i)

# Q22. Sum of Indices of "python" Without range() or len()

text = "python"

index = 0
sum_index = 0

for ch in text:
    sum_index += index
    index += 1

print("Sum of Indices =", sum_index)

# Q23. Count Vowels Without Indexing or Slicing

text = "python programming"

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Total Vowels =", count)

# Q24. Print Repeating Characters in "programming"

text = "programming"

printed = ""

for ch in text:
    if text.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch

# Q25. Find Greatest Character in "01275623"

text = "01275623"

greatest = text[0]

for ch in text:
    if ch > greatest:
        greatest = ch

print("Greatest Character =", greatest)

# Q26. Find First Repeating Character

text = "knowyourself"

seen = ""

for ch in text:
    if ch in seen:
        print("First Repeating Character =", ch)
        break
    seen += ch

# Q27. Print Alternate Words

text = "if you think you can not do, you can not show think wisely"

words = text.split()

for i in range(0, len(words), 2):
    print(words[i])

print("\n")

# Q28. Print Alternate Characters

text = "knowyourself"

position = 0

for ch in text:
    if position % 2 == 0:
        print(ch, end="")
    position += 1

print("\n")

# Q29. Print Number with Odd/Even Label

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start, end + 1):

    if i % 2 == 0:
        print(i, ":Even")
    else:
        print(i, ":Odd")

print("\n")

# Q30. Find Sum of String "198765456412"

text = "198765456412"

total = 0

for ch in text:
    total += int(ch)

print("Sum =", total)

# Q31. Count Digits Greater Than 5

text = "1234567890"

count = 0

for ch in text:
    if int(ch) > 5:
        count += 1

print("Digits greater than 5 =", count)

print("\n")

# Q32. Replace Character in String

text = input("Enter a string: ")

old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

result = ""

for ch in text:
    if ch == old_char:
        result += new_char
    else:
        result += ch

print("Modified String:", result)

print("\n")

# Q33. Replace Spaces with Underscores

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch == " ":
        result += "_"
    else:
        result += ch

print(result)

# Q34. Remove Duplicate Characters

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("Final String:", result)

print("\n")

# Q35. Replace Every Vowel with *

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print(result)

print("\n")

# Q36. Count Only Words (Not Spaces)

text = input("Enter a string: ")

word_count = 0
inside_word = False

for ch in text:

    if ch != " " and inside_word == False:
        word_count += 1
        inside_word = True

    elif ch == " ":
        inside_word = False

print("Number of Words:", word_count)

print("\n")

# Q37. Count Uppercase and Lowercase Letters

text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:

    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)

print("\n")

# Q38. Print Characters at Odd Indices

text = input("Enter a string: ")

for i in range(len(text)):

    if i % 2 != 0:
        print(text[i], end="")

print("\n")

# Q39. Remove All Spaces from String

text = input("Enter a string: ")

result = ""

for ch in text:

    if ch != " ":
        result += ch

print("String without spaces:", result)


# Q40. Count Digits in a String

text = "sytax_error2806 hai"

count = 0

for ch in text:

    if ch.isdigit():
        count += 1

print("Number of Digits:", count)

print("\n")

# Q41. Count Only Alphabets

text = input("Enter a string: ")

count = 0

for ch in text:

    if ch.isalpha():
        count += 1

print("Number of Letters:", count)

# Q42. Banking Balance Tracking

previous_balance = 0

for day in range(1, 11):

    current_balance = day * 100

    print(
        "Day", day,
        ": Balance =", current_balance,
        ", Previous Day Balance =", previous_balance
    )
