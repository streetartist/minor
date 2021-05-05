# Minor Language

https://gitee.com/

## The project we watch
- [pylite](https://github.com/linuxmooc/pylite)
pylite是一个用于编译原理教学的python解释器，通过学习它的源代码可以了解python编译器和虚拟机是如何工作的。

pycom是编译器，由5000行代码构成。pyvm是虚拟机，由6000行代码构成。
- [郑钢《自制编程语言》随书源码及读书笔记](https://github.com/yifengyou/sparrow)
- [Go语法树入门——开启自制编程语言和编译器之旅！](https://github.com/chai2010/go-ast-book)
- [类似与python + cpp语法的x语言，x语言解释器命名为xlang。](https://github.com/lws597/xlang)
- [toypl](https://github.com/ayuLiao/ToyPL/blob/master/lexer.py)
## Demo
[Demo](https://github.com/streetartist/minor/blob/master/Demo.md)

## Grammar
[Grammar](https://github.com/streetartist/minor/blob/master/Grammar.md)

## Subject
[Code Parser](https://github.com/streetartist/minor/blob/master/CodeParser.md)

## Version

```text
version 0.1.1
```

## Rely
[rply](https://pypi.org/project/rply/)


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
