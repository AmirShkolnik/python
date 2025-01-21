
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.choice(friends) # Select a random string directly from the list

print(random_friend)

random_index = random.randint(0, 4)
print(friends[random_index])

print(len(friends))
