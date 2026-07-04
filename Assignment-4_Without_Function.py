# 1. Write a Python program to find the sum of all elements in the list [10, 20, 30, 40, 50].

nums = [10, 20, 30, 40, 50]
total = 0
for num in nums:
    total += num
print("Sum =", total)

# 2. Write a Python program to display the odd and even elements from the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

nums = [10, 23, 11, 12, 33, 44, 2, 5, 6]
print("Even Numbers:")
for num in nums:
    if num % 2 == 0:
        print(num)

print("Odd Numbers:")
for num in nums:
    if num % 2 != 0:
        print(num)

# 3. Write a Python program to count the odd and even numbers in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

nums = [10, 23, 11, 12, 33, 44, 2, 5, 6]
even_count = 0
odd_count = 0
for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even Count =", even_count)
print("Odd Count =", odd_count)

# 4. Write a Python program to interchange the first and last elements in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

nums = [10, 23, 11, 12, 33, 44, 2, 5, 6]
temp = nums[0]
nums[0] = nums[-1]
nums[-1] = temp

print(nums)

# 5. Write a Python program to duplicate all the items in the list li = [1, 2, 3], such that the result is: output = [1, 2, 3, 1, 2, 3, 1, 2, 3].

li = [1, 2, 3]
result = []
for i in range(3):
    for num in li:
        result.append(num)
print(result)

# 6. Find the smallest element in the list [10, 23, 11, 12, 33, 44, 2, 5, 6]. 

nums = [10, 23, 11, 12, 33, 44, 2, 5, 6]
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print("Smallest =", smallest)

# 7. Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64].

nums = [89, 23, 24, 2, 55, 54, 64]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest =", largest)

# 8. Find the repetitive elements in the list [1,2,3,4,56,1,22,23,33,23, 56].

nums = [1,2,3,4,56,1,22,23,33,23,56]
repeated = []
for i in range(len(nums)):
    count = 0

    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1

    if count > 1 and nums[i] not in repeated:
        repeated.append(nums[i])
print(repeated)

# 9. Remove all the odd elements from the list [10, 23, 11,12,33,44,2,5, 6]. 

nums = [10, 23, 11,12,33,44,2,5,6]
even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print(even_nums)

# 10. Find all non-repetitive elements in the list[1,2,3,4,56,1,22,23,33,23,56].

nums = [1,2,3,4,56,1,22,23,33,23,56]
unique = []
for i in range(len(nums)):
    count = 0

    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1

    if count == 1:
        unique.append(nums[i])
print(unique)

# 11. Write a Python program to duplicate all items in the list l = [1, 2, 3] to produce the result: result = [1, 2, 3, 1, 2, 3, 1, 2, 3].

l = [1, 2, 3]
result = []
for i in range(3):
    for num in l:
        result.append(num)
print(result)

# 12. Find the second greatest element in the list [89, 23, 24, 2, 55, 54, 64]. 
nums = [89, 23, 24, 2, 55, 54, 64]
largest = nums[0]
second = nums[0]
for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest =", second)

# 13. Reverse the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56].

nums = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
reverse = []
for i in range(len(nums)-1, -1, -1):
    reverse.append(nums[i])
print(reverse)

# 14. Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in ascending order.

nums = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
print(nums)

# 15. Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in descending order.

nums = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] < nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
print(nums)

# 16. Write a Python program to print all the vowels present in the given list of strings ["Dreamer", "infotech"].

words = ["Dreamer", "infotech"]
for word in words:
    for ch in word:
        if ch in "AEIOUaeiou":
            print(ch)

# 17. Write a Python program to take input from the user to create a list of elements. The user should input each element of the list one by one. Create a list with these elements (maximum of 5 elements).

nums = []
for i in range(5):
    element = input("Enter Element : ")
    nums.append(element)
print("List =", nums)

# for  integer values

nums = []
for i in range(5):
    element = int(input("Enter Element : "))
    nums.append(element)
print(nums)

# 18. Write a Python program to generate a list of numbers in reverse order from 10 to 
# 1 using list comprehension.

numbers = [i for i in range(10, 0, -1)]
print(numbers)

# 19. Create a list of square numbers from 1 to 10 using list comprehension.

squares = [i ** 2 for i in range(1, 11)]
print(squares)

# 20. Create a list of even numbers from 1 to 10 using list comprehension.

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# 21. Filter strings from the list language = ['python', 'php', 'java', 
# 'c++', 'javascript', 'ruby'] that contain a specific letter provided by 
# the user, using list comprehension.

language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby']
letter = input("Enter a letter: ")
result = [word for word in language if letter in word]
print(result)

# 22. Flatten a nested list like [[1,2], [3,4], [5,6]] into a single list.

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for sublist in nested_list for num in sublist]
print(flat_list)

# 23. Find the frequency of each element in a list. 
# List: 
# [1, 2, 2, 3, 4, 1, 5, 2] 
# Output: 
# 1 → 2 times 
# 2 → 3 times 
# 3 → 1 time

numbers = [1, 2, 2, 3, 4, 1, 5, 2]
for num in set(numbers):
    print(num, "->", numbers.count(num), "times")

# 24. Check whether a given list is a palindrome. 
# List: 
# [1, 2, 3, 2, 1] 
# Output: 
# Palindrome

numbers = [1, 2, 3, 2, 1]
if numbers == numbers[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 25. Find the longest string in a list of strings.   
# List:["cat", "elephant", "dog", "hippopotamus"] 
# Output: "hippopotamus"

words = ["cat", "elephant", "dog", "hippopotamus"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

# 26. Count how many strings in a list start with a vowel. 
# List: 
# ["apple", "banana", "orange", "umbrella", "grape", "ice"] 
# Output: 
# 4 strings start with a vowel 
# (apple, orange, umbrella, ice)

words = ["apple", "banana", "orange", "umbrella", "grape", "ice"]
count = 0
for word in words:
    if word[0].lower() in "aeiou":
        count += 1
print(count, "strings start with a vowel")

# 27. Replace all negative numbers in a list with zero 
# List: 
# [5, -3, 7, -1, 0, -8, 4] 
# Output: 
# [5, 0, 7, 0, 0, 0, 4]

numbers = [5, -3, 7, -1, 0, -8, 4]
result = [0 if num < 0 else num for num in numbers]
print(result)

# 28. Create a new list containing only prime numbers from a given list.

numbers = [2, 4, 5, 7, 8, 11, 15, 17]
primes = []
for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
print(primes)

# 29. Convert a list of integers into a single integer number (e.g., [1,2,3,4] → 1234).

numbers = [1, 2, 3, 4]
result = int("".join(str(num) for num in numbers))
print(result)

# 30. Group elements of a list based on even and odd indices.

numbers = [10, 20, 30, 40, 50, 60]
even_index = []
odd_index = []
for i in range(len(numbers)):
    if i % 2 == 0:
        even_index.append(numbers[i])
    else:
        odd_index.append(numbers[i])
print("Even Index Elements:", even_index)
print("Odd Index Elements:", odd_index)

# 31. Find the largest even number in a list.

numbers = [11, 24, 17, 42, 30, 9]
largest_even = None
for num in numbers:
    if num % 2 == 0:
        if largest_even is None or num > largest_even:
            largest_even = num
print(largest_even)

# 32. Find the majority element in a list (an element that appears more than n/2 times). 
# List:[2, 2, 1, 2, 3, 2, 2] 
# Output:2

numbers = [2, 2, 1, 2, 3, 2, 2]
n = len(numbers)
for num in set(numbers):
    if numbers.count(num) > n // 2:
        print("Majority Element:", num)
        break

# 33. Find the difference between the maximum and minimum values in a list. 
# List:[10, 4, 7, 2, 15, 6] 
# Output:13

numbers = [10, 4, 7, 2, 15, 6]
difference = max(numbers) - min(numbers)
print(difference)

# 34. Remove every third element from a list.   
# List:[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Output:[1, 2, 4, 5, 7, 8]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for i in range(len(numbers)):
    if (i + 1) % 3 != 0:
        result.append(numbers[i])
print(result)

# 35. Insert an element at every even index of a list. 
# Original List:[1, 2, 3] 
# Element to Insert: 0 
# Output:[0, 1, 0, 2, 0, 3]

numbers = [1, 2, 3]
result = []
for num in numbers:
    result.append(0)
    result.append(num)
print(result)

# 36. Rearrange a list so that positive and negative numbers alternate. 
# List: [1, 2, -3, -4, 5, -6] 
# Output:[1, -3, 2, -4, 5, -6]

numbers = [1, 2, -3, -4, 5, -6]
positive = []
negative = []
for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

result = []

for i in range(len(positive)):
    result.append(positive[i])

    if i < len(negative):
        result.append(negative[i])
print(result)

# 37. Find all pairs of elements in a list whose sum equals a given target number. 
# List = [2, 4, 3, 5, 7, 8, 9] 
# Target = 7 
# Valid pairs:(2, 5),(4, 3)

numbers = [2, 4, 3, 5, 7, 8, 9]
target = 7
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print((numbers[i], numbers[j]))

# 38. Find the Missing Number from a Sequence. 
# List:[1, 2, 4, 5, 6] 
# Expected Range: 1 to 6 
# Output:3 

numbers = [1, 2, 4, 5, 6]
for num in range(1, 7):
    if num not in numbers:
        print("Missing Number:", num)

# 39. Split a List into Chunks of Size 3. 
# List:[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Output:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

chunks = []

for i in range(0, len(numbers), 3):
    chunks.append(numbers[i:i+3])
print(chunks)

# 40. Reverse Each String in a List. 
# List:["python", "java", "script"] 
# Output: ["nohtyp", "avaj", "tpircs"]

words = ["python", "java", "script"]
result = []
for word in words:
    result.append(word[::-1])
print(result)

# 41. Extract All Digits from a List of Strings 
# List:["abc123", "45def", "gh6"] 
# Output:["123", "45", "6"]

words = ["abc123", "45def", "gh6"]
result = []
for word in words:
    digits = ""

    for ch in word:
        if ch.isdigit():
            digits += ch

    result.append(digits)
print(result)

# 42. Find All Anagram Groups in a List of Words. 
# List:["eat", "tea", "tan", "ate", "nat", "bat"] 
# Output:[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for word in words:
    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)
print(list(groups.values()))
