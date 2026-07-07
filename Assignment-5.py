print("Assignment : 5 (::::----String Basics ------:::::)")
print('1. Filter vowels and consonants from the string "How are you sir".')
def filter_vowels_consonants(text) :
    vowels = ""
    consonants = ""
    for ch in text :
        if ch.isalpha() :
            if ch.lower() in "aeiou" :
                vowels += ch
            else :
                consonants += ch
    print("Vowels : ", vowels)
    print("Consonats : ", consonants)
def main() :
    text = "How are you sir"
    filter_vowels_consonants(text)
main()
print('2.  Count vowels and consonants in the string "How are you sir".')
def count_vowels_consonants(text) :
    vowels_count = 0
    consonats_count = 0
    for ch in text :
        if ch.isalpha() :
            if ch.lower() in "aeiou" :
                vowels_count += 1
            else :
                consonats_count += 1
    print("Vowels Counts : ", vowels_count)
    print("Consonats Counts : ", consonats_count)
def main():
    text = "How are you sir"
    count_vowels_consonants(text)
main()
print('3. Reverse the string "How are you sir".')
def reverse_string(text) :
    reverse_string = ""
    for ch in text : 
        reverse_string = ch + reverse_string
    return reverse_string
def main():
    text = "How are you sir"
    result = reverse_string(text)
    print("Original String :" , text)
    print("Reverse String :", result)
main()
print('4. Convert lowercase letters to uppercase in the string "How are you sir".')
def convert_to_upper(text) :
    upper_text = ""
    for ch in text :
        if ch.islower() :
            upper_text += ch.upper()
        else :
            upper_text += ch
    return upper_text
def main() :
    sentence = "How are you sir"
    result = convert_to_upper(sentence)
    print("Original Sentence : ", sentence)
    print("Converted into Upper Case : ", result)
main()
print('5. Remove duplicate letters from the string "this is python programming place".')
def remove_duplicates(text) :
    result = ""
    for ch in text :
        if ch not in result :
            result += ch
    return result
def main():
    text = "this is python programming place"
    output = remove_duplicates(text)
    print("Original String :", text)
    print("Removed Duplicates : ", output)
main()
print('6. Search for a specific character in the string "this is python programming place".')
def search_character(text,char) :
    found = False
    for ch in text :
        if ch == char :
            found = True
            break
    if found :
        print(char, "is present in the string")
    else :
        print(char, "is not present in the string")
def main():
    data = "this is python programming place"
    search_char = input("Enter the chracter to search : ")
    search_character(data,search_char)
main()
print('7. Find the greatest and smallest characters from the string "venugopaliyer".')
def find_greatest_smallest(string) :
    smallest = string[0]
    greatest = string[0]
    for ch in string :
        if ch < smallest :
            smallest = ch
        if ch > greatest :
            greatest = ch
    print("Smallest Chracter in string : ", smallest)
    print("Greatest Chracter in String : ", greatest)
def main():
    text = "venugopaliyer"
    find_greatest_smallest(text)
main()
print('8. Count the total occurrences of a specific letter in the string\n"this is python programming place".')
def count_occurrances(text,letter) :
    count = 0 
    for ch in text :
        if ch == letter :
            count += 1
    print(f"{letter} occurs {count} times")
def main():
    string = "this is python programming place"
    letter = input("Enter Letter to Search : ")
    count_occurrances(string,letter)
main()   
print('9. Replace "python" with "javascript" in the string "python developer python engineer python holder".') 
def replace_word(text) :
    result = text.replace("python","javascript")
    return result
def main():
    data = "python developer python engineer python holder"
    output = replace_word(data)
    print("Original String : ")
    print(data)
    print("Updated String : ")
    print(output)
main()
print('10. Print alternate letters from the string "How are you sir".')
def alternate_letter(text) :
    result = ""
    for i in range(len(text)) :
        if i % 2 == 0 :
            result += text[i]
    return result
def main():
    data = "How are you sir"
    output = alternate_letter(data)
    print("String with Alternate Letter : ", output)
main()
print('11. Convert the string "qwertyuiopasdfghjklzxcvbnm" to "abcdefghijklmnopqrstuvwxyz".')
def convert_string(text):
    result = ""
    for ch in "abcdefghijklmnopqrstuvwxyz" : 
        for letter in text :
            if ch == letter :
                result += letter
    return result
def main():
    data = "qwertyuiopasdfghjklzxcvbnm"
    print("Oroginal Data : ", data)
    print("Converted String : ", convert_string(data))
main()
print("Extra String Questions : ")
print('2. Check if the string is a palindrome (e.g., "madam" → Palindrome, "hello" → Not palindrome)')
def check_palindrome(text) :
    reverse = ""
    for ch in text :
        reverse = ch + reverse
    if text == reverse :
        print(text,"String is Palindrome")
    else :
        print(text,"String is not palindrome")
def main():
    data = input("Enter the string to check : ")
    check_palindrome(data)
main()
print('13. Count spaces, digits, alphabets, and special characters in "Python 3.9 is awesome!!".')
def count_character(text) :
    spaces = 0 
    digits = 0
    alphabets = 0
    special_character = 0 
    for ch in text :
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit() :
            digits += 1 
        elif ch.isspace():
            spaces += 1
        else :
            special_character += 1
    print("Alphabets : ",alphabets)
    print("Specials Chracter : ", special_character)
    print("Digits : ", digits)
    print("Spaces : ", spaces)
def main() : 
    data = "Python 3.9 is awesome!!"
    count_character(data)
main()
print('14. Find the longest word in the string "Python programming is interesting".')
def longest_word(text) :
    words = text.split()
    print(words)
    longest = words[0]
    for word in words :
        if len(word) > len(longest) :
            longest = word
    return longest
def main() : 
    string = "Python programming is interesting"
    result = longest_word(string)
    print("Longest String : ", result)
main()
print('15. Capitalize the first letter of each word in "welcome to python world".')
def capitalize_word(text) :
    result = ""
    for word in text.split() :
        result += word.capitalize() + " "
    return result
def main() : 
    string = "welcome to python world"
    output = capitalize_word(string)
    print("Original String : ", string)
    print("Capitalize String : ", output)
main()
print('16. Remove all spaces from "How are you sir".')
def remove_spaces(text) : 
    result = ""
    for ch in text : 
        if ch != " " : 
            result += ch 
    return result 
def main() :
    data = "How are you sir"
    output = remove_spaces(data)
    print("Original String : ", data)
    print("After Removing Spaces in String : ", output)
main()
print('18. Sort characters alphabetically in "programming" → "aggimmnoprr".')
def sort_string(text):
    text = list(text)
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] > text[j]:
                text[i], text[j] = text[j], text[i]
    result = ""
    for ch in text:
        result += ch
    print(result)
def main():
    data = "programming"
    sort_string(data)
main()
print('19. Swap cases of all letters in "Python Is Fun" → "pYTHON iS fUN".')
def swap_case(text):
    result = ""
    for ch in text:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    print(result)
def main():
    data = "Python Is Fun"
    swap_case(data)
main()
print("20. Find frequency of each character in \"banana\" → { 'b':1, 'a':3, 'n':2 }.")
def frequency(text):
    checked = ""

    for ch in text:
        if ch not in checked:
            count = 0

            for letter in text:
                if ch == letter:
                    count += 1

            print(ch, ":", count)
            checked += ch
def main():
    data = "banana"
    frequency(data)
main()
print('21. Remove vowels from "How are you sir" → "Hw r y sr".')
def remove_vowels(text):
    result = ""
    for ch in text:
        if ch.lower() not in "aeiou":
            result += ch
    return result
def main():
    data = "How are you sir"
    output = remove_vowels(data)
    print("Original String :", data)
    print("After Removing Vowels :", output)
main()
print('22. Check if a substring exists in "Python programming" (e.g., "thon" → Found).')
def check_substring(text, sub):
    if sub in text:
        print("Found")
    else:
        print("Not Found")
def main():
    data = "Python programming"
    substring = input("Enter substring: ")
    check_substring(data, substring)
main()
print('23. Print words in reverse order in "How are you sir" → "sir you are How".')
def reverse_words(text):
    words = text.split()
    for i in range(len(words) - 1, -1, -1):
        print(words[i], end=" ")
def main():
    data = "How are you sir"
    reverse_words(data)
main()
print('24. Count words in the string "This is a python assignment".')
def count_words(text):
    count = 1
    for ch in text:
        if ch == " ":
            count += 1
    print("Total Words :", count)
def main():
    data = "This is a python assignment"
    count_words(data)
main()
print('25. Find the ASCII value of each character in "ABcd".')
def ascii_value(text):
    for ch in text:
        print(ch, ":", ord(ch))
def main():
    data = "ABcd"
    ascii_value(data)
main()
print('26. Convert a string into a list of words using "split()" (e.g., "Python is fun" → ["Python", "is", "fun"]).')
def convert_list(text):
    words = text.split()
    print(words)
def main():
    data = "Python is fun"
    convert_list(data)
main()
print('27. Join a list of words into a string using "join()" (e.g., ["Python", "is", "fun"] → "Python is fun").')
def join_string(words):
    result = " ".join(words)
    print(result)
def main():
    data = ["Python", "is", "fun"]
    join_string(data)
main()
print('28. Find the first non-repeating character in "swiss" → "w".')
def first_non_repeating(text):
    for ch in text:
        if text.count(ch) == 1:
            print("First Non-Repeating Character :", ch)
            break
def main():
    data = "swiss"
    first_non_repeating(data)
main()
print('29. Check if two strings are anagrams (e.g., "listen" and "silent" → Anagrams).')
def check_anagram(str1, str2):
    if len(str1) != len(str2):
        print("Not Anagrams")
        return
    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            print("Not Anagrams")
            return
    print("Anagrams")
def main():
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    check_anagram(string1, string2)
main()
print('30. Replace all spaces with hyphens (-) in "Python is easy to learn" → "Python-is-easy-to-learn".')
def replace_space(text):
    result = ""
    for ch in text:
        if ch == " ":
            result += "-"
        else:
            result += ch
    return result
def main():
    data = "Python is easy to learn"
    output = replace_space(data)
    print("Original String :", data)
    print("Updated String  :", output)
main()
print("Substring Related Questions")
print('31. Extract a substring from "Python Programming" → from index 0 to 6 should give "Python".')
def extract_substring(text):
    result = ""
    for i in range(0, 6):
        result += text[i]
    return result
def main():
    data = "Python Programming"
    output = extract_substring(data)
    print("Original String :", data)
    print("Substring :", output)
main()
print('32. Check if one string is a substring of another (e.g., "gram" is a substring of "Programming").')
def check_substring(text, sub):
    found = False
    for i in range(len(text) - len(sub) + 1):
        if text[i:i + len(sub)] == sub:
            found = True
            break
    if found:
        print("Substring Found")
    else:
        print("Substring Not Found")
def main():
    data = "Programming"
    substring = input("Enter substring: ")
    check_substring(data, substring)
main()
print('33. Find all occurrences of a substring in "This is Python and Python is fun" → Substring "Python".')
def find_occurrences(text, sub):
    found = False
    for i in range(len(text) - len(sub) + 1):
        if text[i:i + len(sub)] == sub:
            print("Found at index:", i)
            found = True
    if not found:
        print("Substring Not Found")
def main():
    data = "This is Python and Python is fun"
    substring = input("Enter substring: ")
    find_occurrences(data, substring)
main()
print('34. Replace a substring in "I like Python" → Replace "Python" with "Java".')
def replace_substring(text, old, new):
    result = ""
    for word in text.split():
        if word == old:
            result += new + " "
        else:
            result += word + " "
    return result.strip()
def main():
    data = "I like Python"
    output = replace_substring(data, "Python", "Java")
    print("Original String :", data)
    print("Updated String  :", output)
main()
print('35. Remove a substring from "HelloWorld" → Remove "World" → "Hello".')
def remove_substring(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+5] == "World":
            i += 5    
        else:
            result += text[i]
            i += 1
    print("Original String :", text)
    print("Updated String  :", result)
def main():
    data = "HelloWorld"
    remove_substring(data)
main()
print('36. Count occurrences of a substring in "banana" → Substring "ana" appears 2 times.')
def count_substring(text, sub):
    count = 0
    for i in range(len(text) - len(sub) + 1):
        if text[i:i+len(sub)] == sub:
            count += 1
    print("Substring Count :", count)
def main():
    data = "banana"
    substring = "ana"
    count_substring(data, substring)
main()
print('37. Check if a string starts with a substring (e.g., "Python is easy" starts with "Python").')
def check_startswith(text, sub):
    found = True
    if len(sub) > len(text):
        found = False
    else:
        for i in range(len(sub)):
            if text[i] != sub[i]:
                found = False
                break
    if found:
        print("String starts with", sub)
    else:
        print("String does not start with", sub)
def main():
    data = "Python is easy"
    substring = input("Enter substring: ")
    check_startswith(data, substring)
main()
print('38. Check if a string ends with a substring (e.g., "Learn coding" ends with "coding")')
def check_endswith(text, sub):
    found = True
    if len(sub) > len(text):
        found = False
    else:
        start = len(text) - len(sub)
        for i in range(len(sub)):
            if text[start + i] != sub[i]:
                found = False
                break
    if found:
        print("String ends with", sub)
    else:
        print("String does not end with", sub)
def main():
    data = "Learn coding"
    substring = input("Enter substring: ")
    check_endswith(data, substring)
main()
print('39. Split a string based on a substring (e.g., "apple,banana,grapes" → Split by "," → ["apple", "banana", "grapes"])')
def split_string(text):
    result = text.split(",")
    print(result)
def main():
    data = "apple,banana,grapes"
    split_string(data)
main()
print('40. Find the index of the first occurrence of a substring in "Programming is great" → Substring "is" → Index 12.')
def first_occurrence(text, sub):
    found = False
    for i in range(len(text) - len(sub) + 1):
        if text[i:i+len(sub)] == sub:
            print("First Occurrence Index :", i)
            found = True
            break
    if not found:
        print("Substring Not Found")
def main():
    data = "Programming is great"
    substring = input("Enter substring: ")
    first_occurrence(data, substring)
main()
print('41. Find the index of the last occurrence of a substring in "Programming in Python Programming" → Substring "Programming".')
def last_occurrence(text, sub):
    index = -1
    for i in range(len(text) - len(sub) + 1):
        if text[i:i+len(sub)] == sub:
            index = i
    if index != -1:
        print("Last Occurrence Index :", index)
    else:
        print("Substring Not Found")
def main():
    data = "Programming in Python Programming"
    substring = input("Enter substring: ")
    last_occurrence(data, substring)
main()
print('42. Extract substring after a specific word (e.g., "Welcome to Python World" → substring after "to" → "Python World").')
def substring_after_word(text, word):
    found = False
    result = ""
    words = text.split()
    for w in words:
        if found:
            result += w + " "
        if w == word:
            found = True
    print("Original String :", text)
    print("Substring :", result.strip())
def main():
    data = "Welcome to Python World"
    search_word = input("Enter the word: ")
    substring_after_word(data, search_word)
main()
print('43. Extract substring before a specific word (e.g., "Welcome to Python World" → substring before "Python" → "Welcome to")')
def substring_before_word(text, word):
    result = ""
    words = text.split()
    for w in words:
        if w == word:
            break
        result += w + " "
    print("Original String :", text)
    print("Substring :", result.strip())
def main():
    data = "Welcome to Python World"
    search_word = input("Enter the word: ")
    substring_before_word(data, search_word)
main()
print('44. Check if two strings are rotations (cyclic substrings) of each other (e.g., "abcd" and "cdab" → Rotations).')
def check_rotation(str1, str2):
    if len(str1) != len(str2):
        print("Not Rotations")
        return
    temp = str1 + str1
    found = False
    for i in range(len(temp) - len(str2) + 1):
        if temp[i:i + len(str2)] == str2:
            found = True
            break
    if found:
        print("Rotations")
    else:
        print("Not Rotations")
def main():
    string1 = input("Enter First String : ")
    string2 = input("Enter Second String : ")
    check_rotation(string1, string2)
main()
print('45. Find the longest common substring between two strings (e.g., "abcdxyz" and "xyzabcd" → Longest common substring = "abcd").')
def longest_common_substring(str1, str2):
    longest = ""
    for i in range(len(str1)):
        temp = ""
        for j in range(i, len(str1)):
            temp += str1[j]
            if temp in str2:
                if len(temp) > len(longest):
                    longest = temp
    print("Longest Common Substring :", longest)
def main():
    string1 = input("Enter First String : ")
    string2 = input("Enter Second String : ")
    longest_common_substring(string1, string2)
main()