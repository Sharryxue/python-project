# 9-3 用户: 创建一个名为User的类,其中包含属性first_name,和 last_name,还有用户简介通常会使用的其他的几个属性.在类User中定义一个名为describe_user的方法,它打印用户信息摘要;再定义一个名为greet_user()的方法;他向用户发出个性化问候.
# 创建多个表示不同用户的实例,并对每个实例都调用上述两个方法.

class Users():
    """用户初始化"""
    def __init__(self,first_name,last_name,age,gender,hobby,login_attempts=0):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.hobby=hobby
        self.login_attempts=login_attempts


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

    """将用户尝试登录次数+1"""
    def increment_login_attempts(self):
        self.login_attempts += 1

    """将用户尝试登录次数重置为0"""
    def reset_login_attempts(self):
         self.login_attempts=0

user_alan=Users(first_name='alan',last_name='zhang',age='30',gender='male',hobby='coding')
user_alan.describe_user()
user_alan.greet_user

user_sharry=Users(first_name='sharry',last_name='shi',age='30',gender='famale',hobby='sleeping')
user_sharry.describe_user()
user_sharry.greet_user


# 9-5 尝试登录次数: 在为完成9-3而编写的User类中,添加一个名为login_attempts的属性.编写一个名为increment_login_attempts()的方法,它将属性login_attempts的值加1,再编写一个名为reset_login_attempts()的方法,它将属性login_attempts的值重置为0.
# 根据User类创建一个实例,再调用方法increment_logn_attemps(),并再次打印属性login_attempts的值,确认它被重置为0.

user_alan.increment_login_attempts()
print(user_alan.first_name + " " + user_alan.last_name + "has tried " + str(user_alan.login_attempts) + " time(s) to login.")
user_alan.reset_login_attempts()
print(user_alan.first_name + " " + user_alan.last_name + "'s login attempt time is reset as " + str(user_alan.login_attempts ) + ".")

"""Try the attemp increment works as expected."""
user_alan.increment_login_attempts()
print(user_alan.first_name + " " + user_alan.last_name + "has tried " + str(user_alan.login_attempts) + " time(s) to login.")
user_alan.increment_login_attempts()
print(user_alan.first_name + " " + user_alan.last_name + "has tried " + str(user_alan.login_attempts) + " time(s) to login.")