class Father:
    def __init__(self):
        self.a = 'hello'
        self.b = 'world'

    def t(self):
        c = "i'am find'"
        return c

class Child(Father):
    def __init__(self):
        # 调用父类的构造函数
        Father.__init__(self)
        self.d = Father.t(self)


    def t1(self):
        return self.a, self.d

    def t(self):
       super().t()

if __name__ == '__main__':
    # Father = Father()
    # print(Father.a, Father.b, Father.t())
    C = Child()
    print(C.a, C.b, C.d)
    # print(C.t())
