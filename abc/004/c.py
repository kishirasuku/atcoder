s = ["1","2","3","4","5","6"]
n = input()

for i in range(n):
    pick = i % 5
    s[pick],s[pick+1] = s[pick+1],s[pick]

print "".join(s)







