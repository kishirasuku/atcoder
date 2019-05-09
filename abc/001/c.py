def main():
    deg,dis=map(int,raw_input().split())
    if(discheck(dis) == 0):
        print "C",0
    else:
        print degcheck(deg),discheck(dis)
    

def degcheck(deg):
    deglist=[
        ["N",0,11.25],
        ["NNE",11.25,33.75],
        ["NEF",33.75,56.25],
        ["ENE",56.25,78.75],
        ["E",78.75,101.25],
        ["ESE",101.25,123.75],
        ["SE",123.75,146.25],
        ["SSE",146.25,168.75],
        ["S",168.75,191.25],
        ["SSW",191.25,213.75],
        ["SW",213.75,236.25],
        ["WSW",236.75,258.75],
        ["W",258.75,281.25],
        ["WNW",281.25,303.75],
        ["NW",303.75,326.25],
        ["NNW",326.25,348.75],
        ["N",348.75,0]
    ]
    for i in range(len(deglist)):
        if(deglist[i][1]*10 <= deg and deg < deglist[i][2]*10):
            return deglist[i][0]

def discheck(dis):
    dis2=custom_round(float(dis)/60,2)
    dislist=[
        [0,0.0,0.24],
        [1,0.25,1.54],
        [2,1.55,3.34],
        [3,3.35,5.54],
        [4,5.45,7.94],
        [5,7.95,10.74],
        [6,10.75,13.84],
        [7,13.85,17.14],
        [8,17.15,20.74],
        [9,20.75,24,44],
        [10,24.45,28.44],
        [11,28.45,32.64],
        [12,32.65,200000.0]
    ]
    for i in range(len(dislist)):
        if(dislist[i][1] <= dis2 and dis2 <=dislist[i][2]):
            return dislist[i][0]

def custom_round(number, ndigits=0):
    if type(number) == int:
        return number
    d_point = len(str(number).split('.')[1])
    if ndigits >= d_point:
        return number
    c = (10 ** d_point) * 2
    return round((number * c + 1) / c, ndigits)   

main()
