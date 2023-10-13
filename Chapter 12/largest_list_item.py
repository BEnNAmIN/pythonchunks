nums = [1,45,65,65,78,98,400]

def max(list):
    if len(list) == 1:
        print("The Largest number is", list[0])
        
    elif list[0] < list[1]:
        list.remove(list[0])
        max(list)

    elif list[1] < list[0]:
        list.remove(list[1])
        max(list)
    
    elif list[1] == list[0]:
        list.remove(list[1])
        max(list)

max(nums)
    