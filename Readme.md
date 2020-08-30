# Minor Language

## Grammar
[Grammar](https://github.com/streetartist/minor/Grammar.md)

## version

```text
version 0.1.1
```

## rely
[rply](https://pypi.org/project/rply/)

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

## Usage

build-in function:

- `print`:
  ```
  >>> print, 'hello\npeter'
  ... hello
    . peter
  ```
- `quit`:
  ```
  >>> $quit
  ```

## How to test
Run the command to test at the root of this project (the sign `$` means the
prompt of `Linux`):
```shell
$ make test
```

if your computer do not have the command `make`, please click
[here](https://www.gnu.org/software/make/) for more infomations.

## TODO

- command `print`:
  ```minor
  >>> print, "this", "that", " ", 1 + 5 * 10
  ... thisthat 51
  ```

- add a test for `AST/string`

- command `if-elif-else`
  ```minor
  if n > 1:
    do something
  elif n < 1:
    do something
  else:
    do something
  ```

- command `type`
  ```minor
  type:
    text
    number
    bool
    var
    int\float\...
  ```
- on C++
