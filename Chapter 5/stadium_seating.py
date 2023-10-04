def tix():
    a = int(input("how many class A tickets were sold?: "))
    b = int(input("how many class B tickets were sold?: "))
    c = int(input("how many class C tickets were sold?: "))
    a *= 20
    b *= 15
    c *= 10
    print("$"+ str(a + b + c), "were made in tickets sales.")
tix()