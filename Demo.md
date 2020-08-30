# 程序示例

## 猜数游戏
```minor
# 猜数游戏
print "猜数游戏"

answer = random 1 100
until
    if guess := input "请输入一个数" > answer
        print "大了"
    elif guess < answer
        print "小了"
    else return true
print "猜对了"
```
