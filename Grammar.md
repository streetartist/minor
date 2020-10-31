# Minor语言的语法

#TODO

- MTD3 加入Ruby的语法

# 启发
***受到```Red``` ```Python``` ```Rust``` ```C++``` ```C#``` ```Julia```语言的启发***

# 分隔符
- 缩进
- 可以（但不强制）使用 ***;***

# 代码块
{

}

# 注释
- 单行 #
- 多行 ''' '''
- 一定范围 < >

# 变量类型
- 不声明 同Python
- let [const] <变量名>

自动判断类型

const表示不可更改
- 用<变量名>::<类型>进行声明 

类型有 u32 u64 i32 i64 char string等等
- 保留指针

# 输出
- 换行输出```print```
- 输出```put```

# 输入
- ```input```

# 分支
***:可省略***
- if-elif-else 同Python
- unless 相当于if not
- switch
```minor
switch 15:
    10：
        print("是10")
        break
    default:
        print("都不是")
```
- case
```minor
case 15:
    10：
        print "是10"
    default:
        print "都不是"
```
- either
```minor
either <条件>:
    <为真做什么>
：#不可省略
    <为假做什么>
```

# 循环
- while循环
```minor
while <条件>:
    <为真执行>
```
- loop
```minor
loop <次数> :
    <执行>
```
- repeat
```minor
repeat <变量> <次数>: # 每次加一
    <执行>
```
- until
```minor
until:
    <执行到返回true为止>
    <返回>
```

- for
```minor
for i = 1; i < 10; i++:
    print i
```
- foreach 

foreach 数组/字符串变量名

# 文件
***%表示一个文件（其实是一个对象，有size等属性方法）***
```minor
read a := %./我是一个文件.txt
print a # 默认存储内容
write/append "一段追加的文字" a # /表示额外的选项
```
***:=同Python3.8以上海象运算符***

# 函数
```
function <函数名> <参数>：
    <执行>
    <return 返回>
```
```
<函数名>/额外操作名：
    定义额外操作
```

# 类
python中去除()

# 数据类型
字典、列表、元组为Python和Red合成的风格

取值时默认为第一个值

可用 next last 等移动

全部用/all

保留Python推导式、生成器、协程

变量名::<类型>[大小] 定义一个固定大小的数组

# 异常处理
同 Python

# 可以调用其它语言
比如 C++ Python

# 图形界面
Red []改为{}
