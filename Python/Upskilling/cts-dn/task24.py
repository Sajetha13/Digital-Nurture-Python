from math import *
def smtg(num):
    if num<=0:
        print("Number should be greater than 0")
        return
    return sqrt(num), pow(num, 3), log(num)
result = smtg(10)
sqrt_result, cube_result, log_result = result
print(f"Square root: {sqrt_result:.2f}, Cube: {cube_result:.2f}, Logarithm: {log_result:.2f}")