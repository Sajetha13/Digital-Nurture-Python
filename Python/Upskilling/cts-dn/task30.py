def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:   
        print("Both inputs must be numbers")
print(divide(10, 2)) 
(divide(10, 0))
(divide(10, "a"))

        