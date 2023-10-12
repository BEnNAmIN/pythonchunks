import random

rpsch = ["Rock", "Paper", "Scissors"]
pl_ch = input("Rock, Paper, or Scissors?(Capitalize): ")
pl_ch = rpsch.index(pl_ch)

def rps(pl_ch):
    # cp_ch = random.randint(0,2)
    cp_ch = 0
    print("You Chose", rpsch[pl_ch])
    print("I Chose", rpsch[cp_ch])
    print("")
    if [(pl_ch - 2) == cp_ch] or [(pl_ch + 1) == cp_ch]:
        print("You Win :O")

    elif pl_ch == rpsch[cp_ch]:
        print("One more time")
        print("")

        pl_ch = input("Rock, Paper, or Scissors?(Capitalize): ")
        rps(pl_ch)

    else:
        print("I win >:)")

rps(pl_ch)

# print((rpsch.index(pl_ch)+ 1))
# print(rpsch[(rpsch.index(pl_ch)+ 1)])
# print(rpsch.index(pl_ch)-2)