# 6-1 人: 使用一个字典来存储一个熟人的信息,包括名,姓,年龄和居住的城市. 该字典应该包含键 first_name, last_name,age和city.将存储在该字典中的每项信息都打印出来.

person = {
    "first_name":"alan",
    "last_name":"zhang",
    "age":"36",
    "city":"DL"
}

print("My most favorite person named " + person["first_name"].title())
print("He is " + str(person["age"]) + " years old.")

person["gendar"]="Male"
print(person)

person["age"]="37"
print(person)

for key,value in person.items():
    print("\nKey:" + key)
    print("Value:" + value)



# 6-2 喜欢的数字: 使用一个字典来存储一些人喜欢的数字.请想出5个人的名字,并将这些名字用作字典中的键;想出每个人喜欢的一个数字,并将这些数字作为值存储在字典中.打印每个人的名字和喜欢的数字.为让这个程序更有趣,通过询问朋友确保这些数据是真实的.

favorite_num = {
    "Alan": "6",
    "Bill":"8",
    "Caris":"10",
    "Dail":"0"
}

for name, num in favorite_num.items():
    print (name + "'s favorate number is " + num + ".")

print (favorite_num.items())
print (favorite_num["Alan"])

print (favorite_num.keys())
print (favorite_num.values())



# 6-3 词汇表: Python 字典可用于模拟现实生活中的字典,但为避免混淆,我们将后者称为词汇表.
# 想出你在前边学会的五个编程词汇及含义.为此,你可以先打印词汇,在它后面加上一个冒号,再打印词汇的含义;也可在一行打印词汇,再使用换行符(\n)插入一个空行,然后在下一行以缩进的方式打印词汇的含义.

code_name = {
    "列表":"列表由一系列按特定顺序排列的元素组成.列表放在方括号中.",
    "元组":"不可变的列表被称为元组,元组看起来像列表,但是由圆括号来表示.",
    "字典":"字典是一系列键-值对.字典放在花括号中.",
    "函数":"函数是带名字的代码块,用于完成具体的工作.",
    "类":"表示现实世界的事务或情形,编写类时,定义一大类都有的通用行为.",
}

"""同行加冒号':'显示."""
for name, meaning in code_name.items():
    print(name + ":" + meaning)

"""换行缩进显示."""
for name,meaning in code_name.items():
    print(name + "\n" + "   " + meaning)