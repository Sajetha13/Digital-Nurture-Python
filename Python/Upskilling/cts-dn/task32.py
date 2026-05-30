list=[100, 250, 75]
def printval(list):
    if not list:
        print("List is empty")
        return
    for i in list:
        print(i, end =" ")
printval(list)

def appendlist(list, val):
    if val<= 0:
        print("Value should be greater than 0")
        return
    list.append(val)
appendlist(list, 300)
print()
printval(list)