import random

state_caps = {'Alaska':'Juneau','Texas':'Austin','California':'Sacramento','Montana':'Helena',
              'New Mexico':'Sante Fe','Arizona':'Pheonix','Nevada':'Carson City','Colorado':'Denver',
              'Oregon':'Salem','Wyoming':'Cheyenne','Michigan':'Lansing','Minnesota':'St. Paul',
              'Utah':'Salt Lake City','Idaho':'Boise','Kansas':'Topeka','Nebraska':'Lincoln',
              'South Dakota':'Pierre','Washington':'Olympia','North Dakota':'Bismarck',
              'Florida':'Tallahassee','Oklahoma':'Oklahoma City','Missouri':'Jefferson City',
              'Georgia':'Atlanta','Illinois':'Springfield','Iowa':'Des Moines','New York':'Albany',
              'North Carolina':'Raleigh','Virginia':'Richmond','Arkansas':'Little Rock',
              'Alabama':'Montgomery','Louisiana':'Baton Rouge','Mississippi':'Jackson',
              'Pennsylvania':'Harrisburg','Ohio':'Columbus','Tennessee':'Nashville',
              'Kentucky':'Frankfort','Maine':'Augusta','Indiana':'Indianapolis',
              'South Caroline':'Columbia','West Virginia':'Charleston','Maryland':'Annapolis',
              'Hawaii':'Honolulu','Massachussetts':'Boston','Vermont':'Montpelier',
              'New Hampshire':'Concord','New Jersey':'Trenton','Connecticut':'Hartford',
              'Delaware':'Dover'}
x = 49

states = list(state_caps)
game_state = states[random.randint(0,x)]
correct_cap = state_caps.pop(game_state,)

def game(user_choice):
    if user_choice == correct_cap:
        print("nice")
        return True
    else:
        print("nuh uh")
        return False

y = 'y' 
user = input("What is the capitol of " + game_state + ": ")
while y == "y":
    if game(user) == False:
        user = input("What is the capitol of " + game_state + ": ")
        game(user)
    else:
        y = input('keep going? (y/n): ')
        if y == 'y':
            states = list(state_caps)
            game_state = states[random.randint(0,x)]
            correct_cap = state_caps.pop(game_state,)
            user = input("What is the capitol of " + game_state + ": ")
        x -= 1
