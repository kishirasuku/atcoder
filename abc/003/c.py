import decimal

n,k=map(int,raw_input().split())
douga=map(int,raw_input().split())
rate=0

douga.sort()

for i in range(len(douga)):
    douga[i]=decimal.Decimal(douga[i])
    
for i in range(k*-1,0):
    rate=(rate+douga[i])/2

print rate
