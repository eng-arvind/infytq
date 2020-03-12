import re
test = "arvind&#123"
res = re.sub("\D","",test)
print(res)