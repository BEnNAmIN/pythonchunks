import math
            
def hd_calc(x,y):
    nec_dogs = x * y 
    buns_need = (nec_dogs/8)
    dogs_need = (nec_dogs/10)
    buns_need = math.ceil(buns_need)
    dogs_need = math.ceil(dogs_need)
    bun_leftover = (buns_need * 8) - nec_dogs
    dog_leftover = (dogs_need * 10) - nec_dogs
    print("You will need", buns_need, "packages of buns and", dogs_need, "packages of dogs.")
    print("You will have", bun_leftover, "buns leftover, and", dog_leftover, "dogs leftover.")

p_num = int(input("How Many people are coming to the dog eatery? "))
d_num = int(input("How many dogs will each person partake in? "))

hd_calc(p_num,d_num)