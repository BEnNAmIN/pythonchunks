def cal_calc():
    fat = int(input("how man grams of fat do you eat in a day?: "))
    carbs = int(input("how many grams of carbs do you eat in a day?: "))
    cal_f_fat = fat * 9
    cal_f_carbs = carbs * 4
    print("you consumed ", cal_f_carbs," calories from carbs and ", cal_f_fat," calories from fat" )
yah = "y"
while yah == "y":
    cal_calc()
    yah = input("enter 'y' for another calculation: ")