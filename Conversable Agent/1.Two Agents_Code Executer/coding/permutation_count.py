# filename: permutation_count.py
from collections import Counter
import math

word = "ALGEbRA"
# If case-insensitive: word = word.lower()
# Let's count characters precisely
total_letters = len(word)
counts = Counter(word)

print(f"Word: {word}")
print(f"Total letters: {total_letters}")
print(f"Letter counts: {counts}")

# Calculate permutations of a multiset: n! / (n1! * n2! * ...)
denominator = 1
for count in counts.values():
    denominator *= math.factorial(count)

permutations = math.factorial(total_letters) // denominator

print(f"Total unique permutations: {permutations}")