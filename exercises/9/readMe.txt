9-1 中遇到的问题: 
Issue 1
如下代码
            """初始化属性"""
            self.restaurant_name=restaurant_name,
            self.cuisine_type=cuisine_type
问题:
在声明变量时使用了",", 后期运行程序时遇到ERROR: "TypeError: can only concatenate str (not "tuple") to str"
原因?
原因大概是因为使用","号, Python将对应的变量解释为数组, 在print的时候, 因为将不同类型的字符放在一起所以出现类型不一致的报错

解决:
删除变量后的","即可

Issue 2
如下代码
    """餐厅营业状态"""
    def open_restaurant():
          print("The restaurant is curentlt open for bussiness.")
问题:
在声明变量时使用了",", 后期运行程序时遇到如下报错
Traceback (most recent call last):
  File "c:\Sharry\python-project\exercises\9\restr.py", line 27, in <module>        
    restaurant.open_restaurant()
TypeError: Restaurant.open_restaurant() takes 0 positional arguments but 1 was given
原因
类中的方法定义是必须加形参self, 即使在方法体中不使用任何变量.

解决:
def open_restaurant(self):

9-3 中遇到的问题: 
Issue 1
如下代码
    """用户信息描述"""
    def describe_user(self):

问题:
SyntaxError: expected ':'
原因
忘记了 ":"

解决:
加上":"即可

Issue 2
代码如下:
        if self.gender.title()==Male:
问题
Traceback (most recent call last):
  File "c:\Sharry\python-project\exercises\9\users.py", line 27, in <module>
    user_alan.describe_user()
  File "c:\Sharry\python-project\exercises\9\users.py", line 16, in describe_user
    if self.gender.title()==Male:
                            ^^^^
NameError: name 'Male' is not defined. Did you mean: 'False'?

原因:
此处的 Male 是具体的数值, 所以是字符串. 应放入 ""  中.

解决
改成"Male"即可

Issue 3
代码如下:
    user_alan=Users(first_name='alan',last_name='zhang',age='30',

问题
NameError: name 'Users' is not defined

原因
声明实例时应与class 定义对其, 否则会被处理成内部的方法.

解决
与类对其,删除前边多余的tab.