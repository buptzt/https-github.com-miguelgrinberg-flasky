# -*- coding:UTF-8 -*-
# 创建4个类
# 父类
class myparentclass:
    def method(self):
        return 50

# myparentclass的子类
class parentclass(myparentclass):
    def method1(self):
        print('method1')

# 独立的类
class myclass:
    def method(self):
        return 40

# parentclass的子类
class childclass(parentclass):
    def method2(self):
        print('method2')


print(issubclass(childclass,parentclass))
# 输出结果：True

print(issubclass(childclass,myclass))
# 输出结果：False

print(issubclass(childclass,myparentclass))
# 输出结果：True

print(childclass.__bases__)
# 输出结果：(<class '__main__.parentclass'>,)

print(parentclass.__bases__)
# 输出结果：(<class '__main__.myparentclass'>,)



child = childclass()

print(isinstance(child,childclass))
# 输出结果：True

print(isinstance(child,parentclass))
# 输出结果：True

print(isinstance(child,myparentclass))
# 输出结果：True

print(isinstance(child,myclass))
# 输出结果：False

