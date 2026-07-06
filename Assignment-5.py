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