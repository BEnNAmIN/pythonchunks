rain = []
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

for i in range(12):
    if i > 0:
        h = int(input("Rainfall for the next month:"))
    else:
        h = int(input("Rainfall for the first month:"))

    rain.append(h)

total_rain = 0
for i in rain:
    total_rain += i
print("Total rainfall this year was", total_rain)
print("Average monthy rainfall was", round(total_rain/len(rain),3))
print("The month with the highest total rainfall was", months[rain.index(max(rain))],"and the month with the lowest total rainfall was", months[rain.index(min(rain))])
print(rain)