# Minor Language

## version

```text
version 0.0.0
```

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
