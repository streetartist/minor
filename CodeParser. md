# Code Parser - codeparser

***一个优雅的代码解析器***

*准备写的代码解析器*
*暂时不写英文版文档*

## 函数原型
```python
parse(code, function)
```

## 语法
- $ 关键字
- : 类型（: string, : any, :token）
- . 执行函数（通过传入函数的function字典）
- \- 执行函数，***将返回值写入到源命令中，继续解析***（同上）

## 示例

- ```$ print : string text . print text``` 可解析  ```print "Hello world"```
- - 将"Hello world"赋给变量text，再调用function中"print"键值对应的函数
- ```: token var $ = : any value . savevar var value``` 可解析 ```a = 1```
- - 调用"savevar"（后面都为它的参数）
- ```$ input : string text - input text``` 可解析 ```input "请输入:"```
- - 调用"input" ***写入返回值***

## 注意

*为了解析简单快速，Code parser规定每个单词之间必须有一个空格：*
*例如：*
- 不是 ```$print``` 而是 ```$ print```
- 不是 ```:string``` 而是 ```: string```
- 不是 ```.print``` 而是 ```. print```
