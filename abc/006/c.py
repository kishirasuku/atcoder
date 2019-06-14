def main():
    human_num,foot_num = map(int,raw_input().split())

    for baby in range(human_num,-1,-1):
        if baby*4 == foot_num:
            if baby == human_num:
                print 0,0,baby
                return
        else:
            for g in range(human_num-baby,-1,-1):
                if baby*4 + g*3 == foot_num:
                    if baby + g == human_num:
                        print 0,g,baby
                        return
                else:
                    for adult in range(human_num-baby-g,-1,-1):
                        if baby*4 + g*3 + adult*2 == foot_num:
                            if baby + g + adult == human_num:
                                print adult,g,baby
                                return

    print -1,-1,-1

main()



