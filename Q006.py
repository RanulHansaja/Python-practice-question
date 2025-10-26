print("Generate Multiplication Table")

number = int(input("Enter the Number :"))
count = 0

for n in range(1, 11, 1):
    count +=1
    print(f"{number} * {count} = ",count*number)
