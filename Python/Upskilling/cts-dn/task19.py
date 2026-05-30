def sumOdd(end):
    if end <= 0:
        print("Number should be greater than 0")
        return
    tot=0
    for i in range(1, end+1):
        if(i%2==0):
            continue
        tot+=i
    return tot
print(sumOdd(10))
