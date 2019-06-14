n = input()

l = [int(i) for i in str(n)]

if(3 in l or n % 3 == 0):
    print "YES"
else:
    print "NO"
