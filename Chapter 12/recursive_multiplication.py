def mult(x,y):
    print(x)
    if y > 0:
        return x + mult(x, y-1)
    else:
        return 0

num1 = int(input("gimme number:) "))
num2 =  int(input("gimme one more:) "))

print(mult(num1, num2))