def prefixsuffix(s):
    mid = len(s) // 2
    first = mid
    last = mid + 1 if len(s) % 2 else mid
    while True:
        if s[:first] == s[last:]:
            break
        else:
            first -= 1
            last += 1
    if len(s[:first]) == 0:
        print("-1")
    else:
        print(len(s[:first]))


st = input()

prefixsuffix(st)
