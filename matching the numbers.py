import random
a = random.randrange(1, 1001)
b = 0

t = 0

while True:
    print("try: " + str(t+1))
    t=t+1
    b = int(input())
    if a > b:
        print("answer is more big")
    elif a == b:
        print("the answer!")
        break
    else:
        print("answer is more small")

print("the end")
