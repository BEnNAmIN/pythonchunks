def even(num):
    num_2 = int(num/2)
    num_2 = num_2 * 2
    if num_2 == num:
        return True
    else:
        return False

pocket = int(input("Give a roulette pocket: "))
if pocket >=1<=10 or pocket >=19<=28:
    if even(pocket) is True:
        print("This pocket is black.")
    else:
        print("That pocket is red")
elif pocket >=11<=18 or pocket >=29<=36:
    if even(pocket) is True:
        print("That pocket is red")
    else:
        print ("That pocket is black")
elif pocket == 0:
    print("That pocket is green")
else:
    print("That isn't a pocket moron :|")