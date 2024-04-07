# 9-3 用户: 创建一个名为User的类,其中包含属性first_name,和 last_name,还有用户简介通常会使用的其他的几个属性.在类User中定义一个名为describe_user的方法,它打印用户信息摘要;再定义一个名为greet_user()的方法;他向用户发出个性化问候.
# 创建多个表示不同用户的实例,并对每个实例都调用上述两个方法.

class Users():
    """用户初始化"""
    def __init__(self,first_name,last_name,age,gender,hobby):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.hobby=hobby

    """用户信息描述"""
    def describe_user(self):
        print("My name is " + self.first_name.title() + " " + self.last_name.title() + ", I'm " + str(self.age) + " years old.")

        if self.gender.title()=="Male":
            print("I'm a Boy.")
        else:
            print("I'm a Girl.")

        print("I like " + self.hobby + ".")

    """问候用户"""
    def greet_user(self):
         print("Hello" + self.first_name.title() + "" + self.last_name.title() + ", nice to meet you in Python.")

user_alan=Users(first_name='alan',last_name='zhang',age='30',gender='male',hobby='coding')
user_alan.describe_user()
user_alan.greet_user

user_sharry=Users(first_name='sharry',last_name='shi',age='30',gender='famale',hobby='sleeping')
user_sharry.describe_user()
user_sharry.greet_user