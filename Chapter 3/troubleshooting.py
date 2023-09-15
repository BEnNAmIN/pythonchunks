def val_checker(x):
    y = int(x)
    if x>y and x-y >= .5:
        x = round(x)
        print(x)
    elif x>y and x-y <.5:
        x += .5
        print(x)
        x = round(x)
        print(x)



num = 4.6
val_checker(num)

