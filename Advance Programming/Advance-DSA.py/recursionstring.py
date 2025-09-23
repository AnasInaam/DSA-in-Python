string = "ABBA"
def rev(string):
    if len(string) <= 1:
        return True
    else :
        if string[0] == string[-1]:
           return rev(string[1:-1])
        else :
            return False

print(rev(string))

        
    