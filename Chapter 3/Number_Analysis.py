def number_analysis():
    num = int(input("Give me an integer: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    num_2 = num/2
    num_2 = int(num_2)
    num_2 = num_2 * 2

    if num_2 == num:
        print("Even")
    else:
        print("Odd")
        
number_analysis()