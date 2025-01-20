
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option number 1
print(random.choice(friends))

# optin number 2
random_index = random.randint(0, 4)
print(friends[random_index])