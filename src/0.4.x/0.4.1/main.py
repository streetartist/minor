from m_lexer import MLexer
from m_parser import MParser
from m_interpreter import Process
import sys


def repl():
    lexer = MLexer()
    parser = MParser()
    env = {}
    program = Process((), env=env)
    code = ""
    put = ">> "
    while True:
        try:
            text = input(put)
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        if text != "":
            code += text
            put = "-- "
        else:
            tokens = lexer.tokenize(code)

            try:
                tree = parser.parse(tokens)
                program.tree = tree
                program.run()
            except TypeError as e:
                if str(e).startswith("'NoneType' object is not iterable"):
                    print("Syntax Error")
                else:
                    print(e)

            code = ""
            put = ">> "


def exec_file():
    lexer = MLexer()
    parser = MParser()
    with open(sys.argv[1]) as opened_file:
        tokens = lexer.tokenize(opened_file.read())

        # for token in tokens:
        #     print(token)

        tree = parser.parse(tokens)
        # print(tree)

        program = Process(tree)
        program.run()
        # print(program.env)



if __name__ == "__main__":
    if len(sys.argv) == 1:
        repl()
    else:
        exec_file()
