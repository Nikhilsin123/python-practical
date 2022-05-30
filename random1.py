import random
print("generating 3 random integer number netween 100 and 999 divisible by 5")
for num in range(3):
  print(random.randrange(100,999,5),end='')
