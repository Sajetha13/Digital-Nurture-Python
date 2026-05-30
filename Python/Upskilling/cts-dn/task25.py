def add(a, b):
    if a <= 0 or b <= 0:
        print("Numbers should be greater than 0")
        return
    return a + b
result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")