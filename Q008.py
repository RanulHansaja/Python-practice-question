print("Create a simple calculator\n")

num1 = int(input("Enter the number one :"))
choise = str(input("Enter your choise :"))
num2 = int(input("Entee the number two :"))


if choise == '+':
    result = num1 + num2
    
elif choise == '-':
    result = num1 - num2
    
elif choise == '/':
    result = num1 / num2
    
elif choise == '*':
    result = num1 * num2
    
else:
    print("Enter the correct choise !")
    
    
print("\nResult =",result)
