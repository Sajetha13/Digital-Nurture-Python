def checkEven(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
number = 8
print(f"{number} is {checkEven(number)}")