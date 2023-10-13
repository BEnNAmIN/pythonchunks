nums = []
for i in range(20):
    num = int(input("Give me a number: "))
    nums.append(num)
t = 0
for i in nums:
    t += i

max = max(nums)
min = min(nums)

print("The total of all 20 numbers is", t)
print("The average of all 20 numbers is", t/20)
print("The smallest number is the group is", min,"while the largest number in the group is", max)
