import random

random.choice(range(10))

for i in range(100):
    print(str(random.choice(range(10))) + " ", end="")


random.choice(list([1,2,3,4]))

random.choice(list((1,2,3,4)))