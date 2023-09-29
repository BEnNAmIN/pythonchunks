adi = int(input("What is the average percent daily increase of the population?: "))
start = int(input("What is the starting number of organisms?: "))
days = int(input("How many days do you want to approximate?: "))
print("Days Approximate\tPopulation")

for i in range(days):
    print(i+1,"\t\t", start )
    start = start*((adi/100)+1)