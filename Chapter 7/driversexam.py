key = ["A","C","A","A","D","B","C","A","C","B","A","D","C","A","D","C","B","B","D","A"]
user = []
file = open('student_answers.txt', 'r')

for i in range(20):
    t = file.readline()
    t = t.strip("\n")
    user.append(t)


def ex_grader():
    list_correct = []
    list_wrong = []
    num_correct = 0
    num_wrong = 0
    
    for i in range(20):
        if key[i] == user[i]:
            num_correct+=1
            list_correct.append(i)
        else:
            num_wrong+=1
            list_wrong.append(i)
    
    if num_correct >= 15:
        
        print("You passed with", num_correct, "correct, and", num_wrong, "wrong.")
        print("Here's what you got right: ")
        
        for i in range(len(list_correct)):
            print(list_correct[i]+1)
        
        print("Here's what you got wrong: ")
        
        for i in range(len(list_wrong)):
            print(list_wrong[i]+1)

ex_grader()
