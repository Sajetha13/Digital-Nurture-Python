import math
def area(rad):
    if(rad<=0):
        print("Radius should be greater than 0")
    return math.pi*rad*rad
print(f"Area of circle with radius 5: {area(5):.2f}")