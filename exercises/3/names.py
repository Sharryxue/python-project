# 将一些朋友的姓名存储在列表中, 将其命名为names.依次访问该列表中的每个元素,从而将每个朋友的姓名都打印出来.

names = ['alan','bill','caris','dail','eric']

print("\n Here are the full list:")
print(names[:])

print("\n Here are names in the list:")

for name in names:
    print(name.title())

    if name.title() == "Alan":
        print("\nHi," + name.title() + "I'm learning the python now.")

print("\n My latest friend is:")
print(names[-1].title())