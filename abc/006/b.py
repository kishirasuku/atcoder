l = [0,0,1]
n =input()

for i in range(3,n):
    l.append((l[i-1]+l[i-2]+l[i-3]) % 10007)

print l[n-1]
