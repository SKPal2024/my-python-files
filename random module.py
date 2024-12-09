import random
x=random.randint(1,2)
print(x)
c=["rock","paper","scissor"]
print(random.choice(c))
print(random.choices(c))
print(random.choices(c))
random.shuffle(c)
print(c)