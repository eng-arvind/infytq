l = input()
l = list(l)
# print(l)
l = [i for i in l if i >='0' and i <= '9']
l = set(l)
l = list(l)
l.sort(reverse = True)
# print(l)
for i in range(len(l) - 1 ,-1,-1):
    if int(l[i]) % 2 == 0:
        l.append(l.pop(i))
        break
else:
    print(-1)
    exit(0)
print("".join(l))