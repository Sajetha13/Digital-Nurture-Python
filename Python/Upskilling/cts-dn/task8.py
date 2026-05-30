
def minmax(list):
    minm = min(list)
    maxm = max(list)
    return minm, maxm
num = [50000, 75000, 62000, 95000]
mm = minmax(num)
print("Min is ",mm[0],"Max is ",mm[1])
    