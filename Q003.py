print("Count vowels in the \n")

text = str(input("Enter the String :"))

vowel = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowel:
        count += 1


print(f"{count} vowels in the text")
