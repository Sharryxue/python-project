# This is a practice of a given example in content, trying to know the difference of var declare.
# 结论: There has no difference to delare the self.battery = Batterry() before of after the super init, in another word, we would get the same result vy adding self.battery = Batterry() in L49 or L53.
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + "" + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can not roll back an odometer!")

    def increace_odometer(self,miles):
        self.odometer_reading+=miles

class Batterry():
    """一次模拟电车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("this car has a" + str(self.battery_size) + " -kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self,make,model,year):
        self.battery = Batterry()
        """初始化父类的属性,再初始化电动汽车特有的属性"""

        super().__init__(make,model,year)
#        self.battery = Batterry()


my_tesla=ElectricCar("tesla","model s","2016")
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size=85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()