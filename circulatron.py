import math
def circulatron():
    radi = int(input("Enter a radius: "))
    A = (radi ** 2)* math.pi
    C = radi * (2 * math.pi)
    print("The Area of a Circle with a Radius of ", radi, "is ", A)
    print("The Circumfrenceof a Circle with a Radius of ", radi, "is", C)
circulatron()