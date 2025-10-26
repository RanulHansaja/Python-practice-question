print("Find the Second largest number\n")

num1 = int(input("Enter the number one :"))
num2 = int(input("Enter the number two :"))
num3 = int(input("Enter the number three :"))

number = [num1, num2, num3]

number.sort(reverse = True)

print("\nSecond Largest Number =",number[1])

