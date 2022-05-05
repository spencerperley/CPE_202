a = [1,2,3,5,6]

print(a.insert(min(enumerate(a), key = lambda a: a[1] < 4 )[0],4))
print(a)