# TASK 7 : String Processing

text = input("Enter a sentence: ")

vowels = consonants = digits = spaces = 0

for ch in text:
    if ch.lower() in 'aeiou':
        vowels += 1
    
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    elif ch.isalpha():
        consonants += 1


print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

print("Total characters (excluding spaces):", len(text.replace(" ", "")))
