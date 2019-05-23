class FooParent(object):
    def __init__(self):
        self.parent = 'i\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)

class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到FooChild 的父类（就是FooParent）, 然后把类B的对象 FooChild 转换为类 FooParent 的对象
        FooParent.__init__(self)
        print('Child')

    def bar(self, message):
        # super(FooChild, self).bar(message)
        FooParent.bar(self, message)
        print('Child bar function')
        print(self.parent)

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('helloworld')