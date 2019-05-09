def main():
    n=input()
    board=map(int,raw_input().split())
    result=[]
    gcd=makegcdlist(n,board)

    for i in range(n):
        if i==0:
            lists=gcd[1]
        else:
            lists=gcd[0]
        for j in range(n):
            if j==i:
                continue
            else:
                lists=list(set(lists) & set(gcd[i]))
        result.append(max(lists))
    print result
    print max(result)

def makegcdlist(n,board):
    gcd=[]
    for i in range(n):
        l=[]
        for j in range(1,board[i]+1):
            if board[i]%j==0 :
                l.append(j)
        gcd.append(l)
    return gcd

main()
    
