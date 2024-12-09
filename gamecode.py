def find_winner(s, game):
    result=[]
    for n in game:
        x = 0
        turn = 1
        i = 1
        while True:
            if turn % 2 == 1:
                x -= i
                if abs(x) > n:
                    result.append("Sakurako")
                    break
            else:
                x += i
                if abs(x) > n:
                    result.append("Kosuke")
                    break
            i += 2
            turn += 1
    return result
s = int(input())
games = [int(input()) for _ in range(s)]
winners = find_winner(s, games)
for winner in winners:
    print(winner)
