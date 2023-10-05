def lpyr(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    else:
        return False

def evnodd(x):
    y = x
    x = int(x/2)
    x*=2
    if x == y:
        return True
    else:
        return False

#Getting inputs for month, date and year
mn=(input("Gimme a Month (pls capitalize): "))
dy=int(input("Gimme a Day of the Month: "))
yr=int(input("Gimme a Year: "))
skip = int(input("How many days should I skip forward: "))
#Creating a list of months so I can convert to a number
mnths = ["January","February","March","April","May","June","July","August","September","October","November"]
mn_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#Returns index of the given month as a integer value
mn = mnths.index(mn) + 1

def dys_lft():
    dy += skip
    dy = (mn_days(mn)- 1) - dy
    if dy < 0:
        mn += 1

        
    

print(mn)

