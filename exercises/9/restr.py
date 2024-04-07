# 9-1 餐馆: 创建一个名为Restaurant的类,其方法 __init__()设置两个属性:restaurant_name 和 cuisine_type.创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法, 其中前者打印前述两项消息,而后者打印一条消息,指出餐馆正在营业.
# 根据这个类创建一个名为restaurant的实例,分别打印其两个属性,再调用前述两个方法.

class Restaurant():
    """餐馆初始化"""
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
            """初始化属性"""
            self.restaurant_name=restaurant_name
            self.cuisine_type=cuisine_type
            self.number_served=number_served

    """描述餐厅名字以及类型"""
    def describe_restaurant(self):
          print('The name of the restaurant is' + self.restaurant_name)
          print("And I'm a restaurant for cooking " + self.cuisine_type)

    """餐厅营业状态"""
    def open_restaurant(self):
          print("The restaurant is curentlt open for bussiness.")

      # 添加一个名为set_number_served()的方法,它让你能够设置就餐人数.调用这个方法并向它传递一个值,然后再次打印这个值.
      # 添加一个名为increace_number_served()的方法,他让你能够将就餐人数递增.调用这个方法并向它传递一个这样的值:你认为这家餐馆每天可能接待的就餐人数.
    """设置就餐人数"""
    def set_number_served(self,number_served):
         self.number_served=number_served

         print("We've served " + str(self.number_served) + " people since we open the business.")

    """添加就餐人数"""
    def increace_number_served(self,increace):
         self.number_served +=increace

restaurant = Restaurant(restaurant_name='Mr Pizza',cuisine_type='pizza')

"""打印两个属性值"""
print(restaurant.restaurant_name, restaurant.cuisine_type)

"""调用类中的方法"""
restaurant.describe_restaurant()
restaurant.open_restaurant()



# 9-2 三家餐馆:根据你完成的练习9-1而编写的类创建三个实例,并对每个实例调用describe_restaurant().
print("This is the code for 9-2 practice.")
"""创建三个实例"""
restaurant_zh = Restaurant(restaurant_name='中餐馆',cuisine_type='fried dishes')
restaurant_In = Restaurant(restaurant_name='GaliGali',cuisine_type='boiling')
restaurant_Kr = Restaurant(restaurant_name='shiguobanfan',cuisine_type='shiguo')


"""分别调用describe_reastaurant方法"""
restaurant_zh.describe_restaurant()
restaurant_In.describe_restaurant()
restaurant_Kr.describe_restaurant()


# 9-4 就餐人数:在为完成练习9-1而编写的程序中,添加一个名为 number_served 的属性,并将其默认值设置为0,根据这个类创建一个名为restaurant的实例;打印有多少人在这家餐馆就餐过,然后修改这个值并再次打印它.
# 添加一个名为set_number_served()的方法,它让你能够设置就餐人数.调用这个方法并向它传递一个值,然后再次打印这个值.
# 添加一个名为increace_number_served()的方法,他让你能够将就餐人数递增.调用这个方法并向它传递一个这样的值:你认为这家餐馆每天可能接待的就餐人数.

print("This is the code for 9-4 practice.")
"""创建一个实例, 并为其变量直接赋值"""
restaurant_serve = Restaurant(restaurant_name='中餐馆',cuisine_type='fried dishes')
print("See how many people we served since openning: " + str(restaurant_serve.number_served))
restaurant_serve.number_served=100
print("See how many people we served since openning: " + str(restaurant_serve.number_served))

"""调用新建的设置就餐人数方法进行赋值"""
restaurant_serve.set_number_served(200)

restaurant_serve.increace_number_served(1000)
print(str(restaurant_serve.number_served) + " people we'd served by today.")