# 9-1 餐馆: 创建一个名为Restaurant的类,其方法 __init__()设置两个属性:restaurant_name 和 cuisine_type.创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法, 其中前者打印前述两项消息,而后者打印一条消息,指出餐馆正在营业.
# 根据这个类创建一个名为restaurant的实例,分别打印其两个属性,再调用前述两个方法.

class Restaurant():
    """餐馆初始化"""
    def __init__(self,restaurant_name,cuisine_type):
            """初始化属性"""
            self.restaurant_name=restaurant_name
            self.cuisine_type=cuisine_type

    """描述餐厅名字以及类型"""
    def describe_restaurant(self):
          print('The name of the restaurant is' + self.restaurant_name)
          print("And I'm a restaurant for cooking " + self.cuisine_type)

    """餐厅营业状态"""
    def open_restaurant(self):
          print("The restaurant is curentlt open for bussiness.")

restaurant = Restaurant(restaurant_name='Mr Pizza',cuisine_type='pizza')

"""打印两个属性值"""
print(restaurant.restaurant_name, restaurant.cuisine_type)

"""调用类中的方法"""
restaurant.describe_restaurant()
restaurant.open_restaurant()
