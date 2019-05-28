n,k=map(int,raw_input().split())
s=raw_input()

s=list(s)

s[k-1] = s[k-1].lower()

s="".join(s)

print s


