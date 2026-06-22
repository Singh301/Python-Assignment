
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


List = ['10', '20', '30', '40', '50']


# for  integer values

nums = []

for i in range(5):
    element = int(input("Enter Element : "))
    nums.append(element)

print(nums)
