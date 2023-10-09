def falling_distance(x):
    d = (x**2)*(4.9)
    d = round(d,2)
    print("If falling for", x, "seconds, then an object will fall", d, "meters.")
for t in range(1,11):
    falling_distance(t)