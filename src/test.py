def isNum(s):
    dotfirst = True
    for i in s:
        if not (i.isdigit() or (i == "." and dotfirst)):
            return False
        if (i == "." and dotfirst):
            dotfirst = False

    return True

print(isNum("3.00r"))
print(float("3.."))