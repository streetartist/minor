# Minor Language

## Grammar
[Grammar](https://github.com/streetartist/minor/blob/master/Grammar.md)

## Subject
[Code Parser](https://github.com/streetartist/minor/blob/master/Codeparser.md)

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
