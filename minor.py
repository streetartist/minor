from src import main

'''
while True:
    input_ = input(">>> ")
    if input_ != "$quit":
        print("...", main.run(input_))
    else:
        break
'''

while(True):
    print(parser.parse(lexer.lex(input(">>>"))).eval())
