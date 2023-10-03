def k_to_m():
    k = int(input("give me a distance in kilometers:"))
    m = k * 0.6124
    print("that is ", m, " miles.")
yah = "y"
while yah == "y":
    k_to_m()
    yah = input("Type 'y' to do another calculation: ")
