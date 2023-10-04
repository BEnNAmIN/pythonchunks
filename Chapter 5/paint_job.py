import math
def paint_calculator():
    w_ft = int(input("How many square feel of wall spaced is going to be painted?: "))
    pnt = math.ceil(w_ft/112)
    pnt_c = (int(input("How much does each gallon of paint cost?: "))) * pnt
    l_c = ((w_ft/112)*8)*35
    print(pnt, "gallons of paint are needed for a total paint cost of $" + str(pnt_c) + ".", "It will take an estimated time of", round(l_c/35,2), "hours ")
    print("for a total labor cost of $" + str(l_c) + ". The total cost of the job will be $" + str(pnt_c + l_c) + ".")
paint_calculator()


