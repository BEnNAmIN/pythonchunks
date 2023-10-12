def kinetic_energy(vel, mass):
    k_e = (mass/2) * (vel*vel)
    print("The object has a kinetic energy of", round(k_e,2), "Joules")

v = int(input("What is the Velocity of the Object?: "))
m = int(input("What is the Mass of the Object?: "))
kinetic_energy(v, m)