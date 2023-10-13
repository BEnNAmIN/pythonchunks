numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
t = 0

for i in numbers:
    if i > 0 and i < 100:
        t += i
        valid_numbers.append(i)
print(valid_numbers)
print(round(t/len(valid_numbers),1))
