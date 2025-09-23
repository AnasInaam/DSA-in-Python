string = "AnBA"
def rev(string):
    if len(string) == 0:
       return string
    return string[1:]+string[0]

print(rev(string))