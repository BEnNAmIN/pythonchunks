def converter():
    num = int(input("Give me a number: "))
    if num <= 3:
        print(num * "I")
    elif num == 4:
        print("IV")
    elif num >= 5 and num <= 8:
        i_val = (num - 5) * "I"
        print("V"+ i_val )
    elif num > 8:
        i_val = (-1*(num - 10)) * "I"
        print(i_val + "X")
converter()