import random


candidates = input()
leader = candidates.split(',')
print(f'New Leader of the Pack is {random.choice(leader).upper()}')
