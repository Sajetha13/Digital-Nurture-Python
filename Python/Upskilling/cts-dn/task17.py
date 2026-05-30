def printnum(num):
    if num<=0:
        print("Number should be greater than 0")
    while num>0:
        print(num, end=" ")
        num-=1
printnum(5)