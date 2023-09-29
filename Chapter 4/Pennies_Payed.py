n = int(input("How many days are you working?: "))
print("Days\tPennies")
print("________________")
p = 1
for i in range(1, n+1):
    print(i, "   \t",p)
    p *= 2
    