def vinesbaby():
    R = int(input("How long is your row: "))
    E = int(input("How long, in feet, is your end post assembly: "))
    S = int(input("How many feet in between each vine: "))
    V = (R-(2*E))/S
    print (V, "vines will fit in your row")
vinesbaby()