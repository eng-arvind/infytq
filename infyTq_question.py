class classA:
    def __init__(self,val1):
        self.value = val1
    def method_a(self):
        return 10+self.value
class classB:
    def __init__(self,val2):
        self.num = val2
    def method_b(self,obj):
        return obj.method_a()+self.num
obj1 = classA(20)
obj2 = classB(30)
print(obj2.method_b(obj1))