
def Oneaway(str1, str2):
    num_edit = 0
    if len(str1) < len(str2):
        long_str = str2
        short_str = str1
    else:
        long_str = str1
        short_str = str2
    if abs(len(str1)-len(str2)) > 1:
        return False
    elif abs(len(str1)- len(str2)) == 1:
        i, j = 0, 0
        while i < len(long_str):
            if i == len(long_str)-1 and num_edit == 0:
                num_edit +=1
                i+=1
            else:
                if long_str[i] != short_str[j]:
                    i+=1
                    num_edit += 1
                else:
                    i+=1
                    j+=1
    else:
        i, j = 0, 0
        while i < len(long_str):
            if long_str[i] != short_str[j]:
                num_edit +=1
            i+=1
            j+=1   
    if num_edit == 1: return True
    return False

print(Oneaway("pale", "plea"))
