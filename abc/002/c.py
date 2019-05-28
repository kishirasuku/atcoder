ax,ay,bx,by,cx,cy = map(float,raw_input().split())

bx = bx - ax
by = by - ay
cx = cx - ax
cy = cy -ay

print abs(bx*cy-by*cx)/2.0
