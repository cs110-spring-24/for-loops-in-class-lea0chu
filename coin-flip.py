import random
#Let's simulate flipping 100 coins and output the results
heads = 0
tails = 0
for flip in range(100): #range(0,100) #range(0,100,1)
    coin = rand.int(1,2)
    if (coin == 1):
        print("heads")
        heads +=1
    else:
        print("tails")
        tails +=1
print(f"After 100 flips, we flipped {heads} heads and {tails} tails")


