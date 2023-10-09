def gcd(x,y):
    rem = x % y
    if rem == 0:
        print("The GCD of", nums[0], "and", nums[1], "is", y)
    else:
        gcd(y,rem)

yah = "y"

while yah == "y": 
    nums = input("Gimme two numbers to find the gcd of(seperate with a comma): ")
    nums.strip(" ")
    nums = nums.split(",")
    gcd(int(nums[0]),int(nums[1]))
    yah = input("Wanna keep going? (y/n): ")