def lpyr(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    else:
        return False

#Getting inputs for month, date and year
mn = (input("Gimme a Month (pls capitalize): "))
dy = int(input("Gimme a Day of the Month: "))
yr = int(input("Gimme a Year: "))
skip = int(input("How many days should I skip forward: "))
#Creating a list of months so I can convert to a number
mnths = ["January","February","March","April","May","June","July","August","September","October","November"]
mn_days = [31,28,31,30,31,30,31,31,30,31,30,31]

#Returns index of the given month as a integer value
mn = mnths.index(mn)+1

def dys_lft():
    dy += skip
    if lpyr(yr) is True:
        mn_days[1] = 29
    x = mn_days[mn-1] - dy
    mn+=1
    while x < 0:
        mn += 1
        x += mn_days[mn]
    dy += abs(x)
dys_lft()

print(mn+1)
print(dy)

