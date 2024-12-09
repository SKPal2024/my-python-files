import random
choices =["rock","paper","scissor"]
comp=random.choice(choices)
print("computer->",comp)
choices1=["r","p","s"]
player= None
while player not in choices1:
    player=input("rock , paper or scissior ->").lower()
if player==comp:
    print("match tied")
elif player=="r":
    if comp=="paper":
        print("computer won")
    if comp=="scissor":
        print("congrats you won")
elif player=="p":
    if comp=="rock":
        print("congrats you won")
    if comp=="scissor":
        print("comp won")
elif player=="s":
    if comp=="rock":
        print("computer won")
    if comp=="paper":
        print("congrats you won")