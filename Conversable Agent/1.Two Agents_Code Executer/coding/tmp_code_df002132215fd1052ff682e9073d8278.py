from math import factorial
from collections import Counter

word = "ALGEbRA"
permutations = factorial(len(word))

for count in Counter(word).values():
    permutations //= factorial(count)

print(permutations)