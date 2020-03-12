s = input()
l = len(s)
unique = ''
for i in range(l):
    substring = s[i]
    for j in range(i + 1, l):
        substring += s[j]
        if 3 <= len(substring) == len(set(substring)):
            if len(unique) < len(substring):
                unique = substring
if len(unique)==0:
    print("-1")
else:
    print(unique)