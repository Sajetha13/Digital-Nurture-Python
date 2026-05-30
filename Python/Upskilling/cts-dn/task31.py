list=[100, 250, 75]
def printval(list):
    if not list:
        print("List is empty")
        return
    for i in list:
        print(i)
printval(list)