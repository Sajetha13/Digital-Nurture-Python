def check(start, end):
    if end <=0:
        print("Number should be greater than 0")
    for i in range(start, end+1):
        if i%2==0:
            print(f"{i} is even")
            break
check(20, 30)