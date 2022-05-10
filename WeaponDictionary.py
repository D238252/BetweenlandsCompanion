# Doin the hashtable sha blam
import random

x = random.randrange(0,10)

print(x)


def hashindex(elem):
    total = 0
    for i in elem:
        total += ord(i)
    return total

sample = "Short Sword"

print(hashindex(sample))
