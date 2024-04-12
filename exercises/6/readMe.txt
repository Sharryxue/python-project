6-1 中遇到的问题: 
Issue 1
如下代码
person = {
    "first_name":"alan"
    "last_name":"zhang"
    "age":"36"
    "city":"DL"
}
问题:
    "last_name":"zhang",
               ^
SyntaxError: invalid syntax

原因
字典声明中, 键值对儿之间未使用逗号","间隔, 导致出现SyntaxError.

解决:
加上","即可