board = []

for i in range(4):
    board.append(raw_input().split())

for l in board:
    l.reverse()

board.reverse()

for l in board:
    for s in l:
        print s,
    print 



