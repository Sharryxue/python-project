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