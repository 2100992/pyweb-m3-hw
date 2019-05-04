def solve():
    s = ''
    for i in range(2000,3200):
        if i % 7 == 0 and i % 5 != 0:
            if s == '':
                s = str(i)
            else:
                s = '%s,%s' % (s, i)
    return s
