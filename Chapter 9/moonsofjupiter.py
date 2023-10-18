moonsjup_r = {'Io':1828.6, 'Europa':1560.8, 'Ganymede':2634.1, 'Calisto':2410.3}
moonsjup_g = {'Io':1.796, 'Europa':1.314, 'Ganymede':1.428, 'Calisto':1.235}
moonsjup_o = {'Io':1.769, 'Europa':3.551, 'Ganymede':7.154, 'Calisto':16.689}
list = [moonsjup_r, moonsjup_g, moonsjup_o]

user_choice = input("Enter a moon of jupiter(Capitalize): ")

def moons_of_jup(choice):
    for i in list:
        if choice in i:
            print(i[choice])

moons_of_jup(user_choice)