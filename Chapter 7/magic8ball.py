import random

responses = []
file = open('magic8ballresponses.txt', 'r')
for i in range(12):
    t = file.readline()
    t = t.strip('\n')
    responses.append(t)

kg = 'y'
while kg=='y':
    question = input("Ask away!: ")
    print(responses[random.randint(1,12)])
    kg = input("Keep going?(y/n): ")
    