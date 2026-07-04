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
        ch == char
        found = True
        break
    if found :
        print(char, "is present in the string")
    else :
        print(char, "is not present in the string")



    
    