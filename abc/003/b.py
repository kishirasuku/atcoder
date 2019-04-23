s=raw_input()
t=raw_input()

for i in range(len(s)):
    if(s[i]==t[i]):
        continue
    elif(s[i] != '@' and t[i] != '@'):
        print "You will lose"
        break 
    else:
        if(s[i] in "atcorder" or t[i] in "atcorder") :
            continue
        else:
            print "You will lose"
            break
else:
    print "You can win"
            
        
