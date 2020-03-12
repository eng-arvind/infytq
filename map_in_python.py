# map(fun,itr)
# fun-> It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
def add(n):
    return n+n
num = (1,2,3,4)
result = list(map(add,num))
print(result)