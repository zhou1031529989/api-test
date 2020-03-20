#反射

"""
静态---运行前，如果要调用类的属性或者方法，我需要实例化它的对象
动态---运行时，我就获取类的属性或者方法，甚至更改他的属性或者方法
"""

class Girls:

    single = False

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def singe(self):
        print(self.name+"会唱歌")

if __name__ == '__main__':
    g = Girls('monge',18)
    print(g.name)   # 获取属性，静态
    g.singe()       # 调用方法，静态

    # 给类动态的去添加属性或者方法，实例对象添加属性，则只有这个实例对象才有这个属性
    # setattr(g,'hob','swimming')   # 属性hob,值swimming,g有hob属性
    # print(g.hob)

    # g2 = Girls('lucy',20)         #g2没有hob属性
    # print(g2.hob)        # AttributeError: 'Girls' object has no attribute 'hob'

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 给类或者实例对象动态的去添加属性或者方法,类增加属性，每一个实例化的对象都会有这个属性
    # setattr(Girls,'hob','swimming')  # g有hob属性
    # print(g.hob)
    #
    # g2 = Girls('lucy',20)            # g2也有hob属性
    # print(g2.hob)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 根据属性名 动态获取类的属性
    setattr(Girls,'hob','swimming')
    print(getattr(Girls,'hob'))

    # 当属性不存在的时候，报错AttributeError: type object 'Girls' has no attribute 'height'，
    # 需要先设置给她一个属性setattr(Girls,'hob','swimming')，然后才能通过getattr获取到该属性
    # print(getattr(Girls,'height'))

    # 判断当前这个类有没有这个属性,有就返回True,没有就返回False
    print(hasattr(Girls,'height'))  # False
    # 初始化函数被调用时，才有name属性
    print(hasattr(Girls,'name'))    # False
    # hasattr判断时，在初始化函数外面定义的属性，才有
    print(hasattr(Girls,'single'))  # True
    print(hasattr(g,'single'))      # True
    # 判断对象是否有这个实例属性
    print(hasattr(g,'name'))        # True
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 删除对象属性
    # delattr(g,'name')
    # print(g.name)      # AttributeError: 'Girls' object has no attribute 'name'

    # 删除类属性
    # delattr(Girls,'single')
    # print(getattr(Girls,'single'))   # AttributeError: type object 'Girls' has no attribute 'single'