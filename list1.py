text = input("enter a string: ")
vowels = 0
consonants = 0
for ch in text:
    if ch.lower() in "aieou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
print ("vowels: ", vowels)
print ("consonants: ", consonants)