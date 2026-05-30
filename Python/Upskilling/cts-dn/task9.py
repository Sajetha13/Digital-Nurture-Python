def display(name):
    if not name:
        print("Name is empty")
    else:
        print(f"Hello, {name}!")
display(input("Enter your name: "))