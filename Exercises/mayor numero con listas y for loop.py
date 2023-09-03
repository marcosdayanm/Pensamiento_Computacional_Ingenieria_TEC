def maxim (l):
    m = 0
    for i in l:
        if i>m:
            m = i
    return m

print(maxim([3,66,889,76765]))