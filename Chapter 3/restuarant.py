vege = input("Is anybody in your party vegeterian? ")
gl_fr = input("Is anybody in your party vegeterian? ")
vega = input("Is anybody in your party vegan? ")

print("Here are your restaurant choices: ")
if vege == "yes" or "Yes":
    if gl_fr == "yes" or "Yes":
        if vega == "yes" or "Yes":
            print("Corner Cafe")
            print("The Chef's Kitchen")
        else:
            print("Corner Cafe")
            print("The Chef's Kitchen")
            print("Main Street Pizza Company")
    elif vega == "yes" or "Yes":
        print("The Chef's Kitchen")
        print("Corner Cafe")
    else:
        print("The Chef's Kitchen")
        print("Corner Cafe")
        print("Main Street Pizza Company")
        print("Mama's Fine Italian Kitchen")
else:
    
