def checker(x,y,z):
    if x*y==z:
        print("That date is Magic :)")
    else:
        print("It's not magic :(")
day = int(input("Give me a numeric date: "))
month = int(input("Give me a numeric month: "))
year = int(input("Give me a two digit year: "))
checker(day,month,year)

