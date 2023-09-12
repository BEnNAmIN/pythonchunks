def comp_int():
    P = int(input("How much money starts in the account: "))
    r = float(input("what is the interest rate: "))
    r /= 100
    n = int(input("How many times is the interest paid per year: "))
    t = int(input("Specify a time frame in years: "))
    A = P*(1 + (r/n))**(n*t)
    print("After ",t, "years, you will have a total of $",A)
comp_int()