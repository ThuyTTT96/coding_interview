def checkValidString(s):
        characters = [["(",")"], ['(', '*'],['*', ')']]
        open_ = []
        star=[]
        if len(s) == 1 and s !="*":
            return False
        for c in range(len(s)):
            if (s[c] == '(') :
                open_.append(c)
            elif (s[c] == '*'):
                star.append(c)
            else:
                if open_!=[]: 
                    open_.pop()
                elif star!=[]:
                    star.pop()
                else:
                    return False
        while open_!=[] and star != []:
            if star[-1] > open_[-1]:
                star.pop()
                open_.pop()
        if open_ == []:
            return True
        else:
            return False

print(checkValidString("(*)"))
