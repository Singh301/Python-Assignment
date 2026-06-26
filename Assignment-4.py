# 1. Write a Python program to find the sum of all elements in the list [10, 20, 30, 40, 50].

def sum_of_all_element(numbers) :
    total = 0
    for num in numbers:
        total += num
    return total
list = [10, 20, 30, 40, 50]
result = sum_of_all_element(list)
print("Sum of all elements : ", result)

# 2. Write a Python program to display the odd and even elements from the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

def display_odd_even(numbers):
    print("Even Numbers:")
    for num in numbers:
        if num % 2 == 0:
            print(num)
    print("Odd Numbers:")
    for num in numbers:
        if num % 2 != 0:
            print(num)
list = [10, 23, 11, 12, 33, 44, 2, 5, 6]
display_odd_even(list)

# 3. Write a Python program to count the odd and even numbers in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Even Count :", even_count)
    print("Odd Count :", odd_count)
list = [10, 23, 11, 12, 33, 44, 2, 5, 6]
count_even_odd(list)

# 4. Write a Python program to interchange the first and last elements in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

def interchange_fisrt_last(numbers) :
    temp = numbers[0]
    numbers[0] = numbers[-1]
    numbers[-1] = temp
    print(numbers)
list = [10, 23, 11, 12, 33, 44, 2, 5, 6]
interchange_fisrt_last(list)

# 5. Write a Python program to duplicate all the items in the list li = [1, 2, 3], such that the result is: output = [1, 2, 3, 1, 2, 3, 1, 2, 3].

def duplicate_all_item(numbers) :
    result = []
    for i in range(3):
        for num in numbers:
            result.append(num)
    print(result)
li = [1, 2, 3]
duplicate_all_item(li)

# 6. Find the smallest element in the list [10, 23, 11, 12, 33, 44, 2, 5, 6]. 

def find_smallest(numbers) :
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    print("Smallest =", smallest)
list = [10, 23, 11, 12, 33, 44, 2, 5, 6]
find_smallest(list)

# 7. Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64].

def find_largest(numbers) :
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print("Largest =", largest)
list = [89, 23, 24, 2, 55, 54, 64]
find_largest(list)

# 8. Find the repetitive elements in the list [1,2,3,4,56,1,22,23,33,23, 56].

def find_repetitive_elements(numbers) :
    repeated = []
    for i in range(len(numbers)):
        count = 0
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1
        if count > 1 and numbers[i] not in repeated:
            repeated.append(numbers[i])
    print(repeated)
list = [1,2,3,4,56,1,22,23,33,23,56]
find_repetitive_elements(list)

# 9. Remove all the odd elements from the list [10, 23, 11,12,33,44,2,5, 6]. 

def remove_all_odd_elements(numbers) :
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num)
    print(even_nums)
list = [10, 23, 11,12,33,44,2,5,6]
remove_all_odd_elements(list)

# 10. Find all non-repetitive elements in the list[1,2,3,4,56,1,22,23,33,23,56].

def find_all_non_repetitive_elements(numbers) :
    unique = []
    for i in range(len(numbers)):
        count = 0
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1
        if count == 1:
            unique.append(numbers[i])
    print(unique)
list = [1,2,3,4,56,1,22,23,33,23,56]
find_all_non_repetitive_elements(list)

# 11. Write a Python program to duplicate all items in the list l = [1, 2, 3] to produce the result: result = [1, 2, 3, 1, 2, 3, 1, 2, 3].

def duplicate_all_item(list) :
    result = []
    for i in range(3):
        for num in list:
            result.append(num)
    print(result)
l = [1, 2, 3]
duplicate_all_item(l)

# 12. Find the second greatest element in the list [89, 23, 24, 2, 55, 54, 64]. 

def second_greatest_element(numbers):
    largest = numbers[0]
    second = numbers[1]

    if second > largest:
        largest, second = second, largest

    for i in range(2, len(numbers)):
        if numbers[i] > largest:
            second = largest
            largest = numbers[i]
        elif numbers[i] > second:
            second = numbers[i]
    print("Second Largest =", second)
list = [89, 23, 24, 2, 55, 54, 64]
second_greatest_element(list)

# 13. Reverse the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56].

def reverse_list(numbers) : 
    reverse = []
    for i in range(len(numbers)-1, -1, -1):
        reverse.append(numbers[i])
    print(reverse)
list = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
reverse_list(list)

# 14. Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in ascending order.

def arrange_list_ascending_order(numbers) :
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    print(numbers)
list = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
arrange_list_ascending_order(list)

# 15. Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in descending order.

def arrange_list_descending_order(numbers) :
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    print(numbers)
list = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
arrange_list_descending_order(list)

# 16. Write a Python program to print all the vowels present in the given list of strings ["Dreamer", "infotech"].

def print_all_vowels(list) :
    for word in list:
        for ch in word:
            if ch in "AEIOUaeiou":
                print(ch)
list_of_string = ["Dreamer", "infotech"]
print_all_vowels(list_of_string)

# 17. Write a Python program to take input from the user to create a list of elements. The user should input each element of the list one by one. Create a list with these elements (maximum of 5 elements).

# for string values :

def create_list_by_user() :
    nums = []
    for i in range(5):
        element = input("Enter Element : ")
        nums.append(element)
    print("List =", nums)
create_list_by_user()

# integer values :

def list_by_user_integer() :
    nums = []
    for i in range(5):
        element = int(input("Enter Element : "))
        nums.append(element)
    print("List =", nums)
list_by_user_integer()

# 18. Write a Python program to generate a list of numbers in reverse order from 10 to 
# 1 using list comprehension.

def reverse_numbers():
    numbers = [i for i in range(10, 0, -1)]
    print(numbers)
reverse_numbers()

# 19. Create a list of square numbers from 1 to 10 using list comprehension.

def squares_numbers() :
    squares = [i ** 2 for i in range(1, 11)]
    print(squares)
squares_numbers()

# 20. Create a list of even numbers from 1 to 10 using list comprehension.

def even_numbers() :
    even_numbers = [i for i in range(1, 11) if i % 2 == 0]
    print(even_numbers)
even_numbers()

# 21. Filter strings from the list language = ['python', 'php', 'java', 
# 'c++', 'javascript', 'ruby'] that contain a specific letter provided by 
# the user, using list comprehension.

def filter_string_specific_latter(list_of_string) :
    letter = input("Enter a letter: ")
    result = [word for word in list_of_string if letter in word]
    print(result)

language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby']
filter_string_specific_latter(language)

# 22. Flatten a nested list like [[1,2], [3,4], [5,6]] into a single list.

def flatten_list(nested_list):
    flat_list = [num for sublist in nested_list for num in sublist]
    return flat_list

nested_list = [[1, 2], [3, 4], [5, 6]]
print(flatten_list(nested_list))

# 23. Find the frequency of each element in a list. 
# List: 
# [1, 2, 2, 3, 4, 1, 5, 2] 
# Output: 
# 1 → 2 times 
# 2 → 3 times 
# 3 → 1 time

def frequency(numbers):
    checked = []

    for num in numbers:
        if num not in checked:
            count = 0

            for item in numbers:
                if item == num:
                    count += 1

            print(num, "->", count, "times")
            checked.append(num)

list = [1, 2, 2, 3, 4, 1, 5, 2]
frequency(list)

# 24. Check whether a given list is a palindrome. 
# List: 
# [1, 2, 3, 2, 1] 
# Output: 
# Palindrome

def palindrome(numbers):
    if numbers == numbers[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
list = [1, 2, 3, 2, 1]
palindrome(list)

# 25. Find the longest string in a list of strings.   
# List:["cat", "elephant", "dog", "hippopotamus"] 
# Output: "hippopotamus"

def longest_string(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
list = ["cat", "elephant", "dog", "hippopotamus"]
print(longest_string(list))

# 26. Count how many strings in a list start with a vowel. 
# List: 
# ["apple", "banana", "orange", "umbrella", "grape", "ice"] 
# Output: 
# 4 strings start with a vowel 
# (apple, orange, umbrella, ice)

def vowel_count(words):
    count = 0
    for word in words:
        if word[0].lower() in "aeiou":
            count += 1
    print(count, "strings start with a vowel")

list = ["apple", "banana", "orange", "umbrella", "grape", "ice"]
vowel_count(list)

# 27. Replace all negative numbers in a list with zero 
# List: 
# [5, -3, 7, -1, 0, -8, 4] 
# Output: 
# [5, 0, 7, 0, 0, 0, 4]

def replace_negative(numbers):
    result = [0 if num < 0 else num for num in numbers]
    return result
list = [5, -3, 7, -1, 0, -8, 4]
print(replace_negative(list))

# 28. Create a new list containing only prime numbers from a given list.

def prime_numbers(numbers):
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
    return primes

list = [2, 4, 5, 7, 8, 11, 15, 17]
print(prime_numbers(list))

# 29. Convert a list of integers into a single integer number (e.g., [1,2,3,4] → 1234).

def list_to_number(numbers):
    return int("".join(str(num) for num in numbers))

numbers = [1, 2, 3, 4]
print(list_to_number(numbers))

# 30. Group elements of a list based on even and odd indices.

def even_odd_index(numbers):
    even_index = []
    odd_index = []

    for i in range(len(numbers)):
        if i % 2 == 0:
            even_index.append(numbers[i])
        else:
            odd_index.append(numbers[i])

    print("Even Index Elements:", even_index)
    print("Odd Index Elements:", odd_index)

list = [10, 20, 30, 40, 50, 60]
even_odd_index(list)

# 31. Find the largest even number in a list.

def largest_even(numbers):
    even = None

    for num in numbers:
        if num % 2 == 0:
            if even is None or num > even:
                even = num
    return even
list = [11, 24, 17, 42, 30, 9]
print(largest_even(list))

# 32. Find the majority element in a list (an element that appears more than n/2 times). 
# List:[2, 2, 1, 2, 3, 2, 2] 
# Output:2

def majority_element(numbers):
    n = len(numbers)

    for num in set(numbers):
        if numbers.count(num) > n // 2:
            print("Majority Element:", num)
            return
numbers = [2, 2, 1, 2, 3, 2, 2]
majority_element(numbers)

# 33. Find the difference between the maximum and minimum values in a list. 
# List:[10, 4, 7, 2, 15, 6] 
# Output:13

def difference(numbers):
    return max(numbers) - min(numbers)

numbers = [10, 4, 7, 2, 15, 6]
print(difference(numbers))

# 34. Remove every third element from a list.   
# List:[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Output:[1, 2, 4, 5, 7, 8]

def remove_third(numbers):
    result = []

    for i in range(len(numbers)):
        if (i + 1) % 3 != 0:
            result.append(numbers[i])

    return result
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(remove_third(list))

# 35. Insert an element at every even index of a list. 
# Original List:[1, 2, 3] 
# Element to Insert: 0 
# Output:[0, 1, 0, 2, 0, 3]

def insert_even_index(numbers, element):
    result = []

    for num in numbers:
        result.append(element)
        result.append(num)

    return result
list = [1, 2, 3]
print(insert_even_index(list, 0))

# 36. Rearrange a list so that positive and negative numbers alternate. 
# List: [1, 2, -3, -4, 5, -6] 
# Output:[1, -3, 2, -4, 5, -6]

def alternate_numbers(numbers):
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

    return result
list = [1, 2, -3, -4, 5, -6]
print(alternate_numbers(list))

# 37. Find all pairs of elements in a list whose sum equals a given target number. 
# List = [2, 4, 3, 5, 7, 8, 9] 
# Target = 7 
# Valid pairs:(2, 5),(4, 3)

def find_pairs(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                print((numbers[i], numbers[j]))
list = [2, 4, 3, 5, 7, 8, 9]
find_pairs(list, 7)

# 38. Find the Missing Number from a Sequence. 
# List:[1, 2, 4, 5, 6] 
# Expected Range: 1 to 6 
# Output:3 

def missing_number(numbers):
    for num in range(1, max(numbers) + 1):
        if num not in numbers:
            print("Missing Number:", num)

list = [1, 2, 4, 5, 6]
missing_number(list)

# 39. Split a List into Chunks of Size 3. 
# List:[1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Output:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def split_chunks(numbers):
    chunks = []

    for i in range(0, len(numbers), 3):
        chunks.append(numbers[i:i + 3])

    return chunks
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(split_chunks(list))

# 40. Reverse Each String in a List. 
# List:["python", "java", "script"] 
# Output: ["nohtyp", "avaj", "tpircs"]

def reverse_strings(words):
    result = []

    for word in words:
        result.append(word[::-1])

    return result
words = ["python", "java", "script"]
print(reverse_strings(words))

# 41. Extract All Digits from a List of Strings 
# List:["abc123", "45def", "gh6"] 
# Output:["123", "45", "6"]

def extract_digits(words):
    result = []

    for word in words:
        digits = ""
        for ch in word:
            if ch.isdigit():
                digits += ch
        result.append(digits)
    return result
words = ["abc123", "45def", "gh6"]
print(extract_digits(words))

# 42. Find All Anagram Groups in a List of Words. 
# List:["eat", "tea", "tan", "ate", "nat", "bat"] 
# Output:[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def anagram_groups(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    for value in groups.values():
        print(value)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_groups(words)