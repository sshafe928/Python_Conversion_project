decimal = float(input("Enter a decimal number:  "))
if decimal.is_integer():
    decimal= int(decimal)
    binary= bin(decimal)
    print("The binary number for " + str(decimal) + " is: " + str(binary))
else:
    print("Enter a valid number")