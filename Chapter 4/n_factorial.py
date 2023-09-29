def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fact(x-1) * x

def main():
    num = int(input("Gimme a number: "))
    print("Heres the factorial of " + str(num) + ":")
    print(fact(num))

main()