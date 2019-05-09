num=input()
value=map(int,raw_input().split())
cost=map(int,raw_input().split())

sums=0

for vi,ci in zip(value,cost):
    if vi > ci:
        sums+=(vi-ci)
print sums

