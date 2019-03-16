def main():
    n=input()
    kushi=map(int,raw_input().split())
    print answer(n,kushi)

def answer(n,kushi):
    kushi.sort()
    kushi.reverse()
    sums=0
    for i in range(1,2*n,2):
        sums+=kushi[i]
    return sums
        

if __name__=='__main__':
    main()
