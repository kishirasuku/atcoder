import calendar

def main():
    today = raw_input()
    today = today.split("/")
    today = [int(s) for s in today ]
    year,month,day = today
    
    while True:
        if daycheck(year,month,day):
            print str(year) + "/" + format(int(month),'02d') + "/" + format(int(day),'02d')
            break
        else:
            if day == calendar.monthrange(year,month)[1]:
                day = 1
                if month == 12 :
                    month = 1
                    year += 1
                else:
                    month += 1
            else:
                day += 1
                    
def daycheck(year,month,day):
    if float(year % month) == 0 :
        if float(year / month) % day == 0:
            return True
        else:
            return False
    else:
        return False
    
main()


