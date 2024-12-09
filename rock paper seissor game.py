import random
choices =["rock","paper","scissor"]
comp=random.choice(choices)
choices1=["r","p","s"]
player= None
while player not in choices1:
    player=input("rock , paper or scissior -> ").lower()
print("computer->",comp)
if comp==player:
    print("match tied")
elif player=="r":
    pass
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
# while True:
#     try:
#         if player == "r":
#            if comp == "paper":
#               print("computer won")
#            if comp == "scissor":
#                print("congrats you won")
#         elif player == "p":
#             if comp == "rock":
#                 print("congrats you won")
#             if comp == "scissor":
#                  print("comp won")
#         elif player == "s":
#             if comp == "rock":
#                   print("computer won")
#             if comp == "paper":
#                    print("congrats you won")
#     except:
#       pass