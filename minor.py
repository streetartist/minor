from src import main

while True:
    input_ = input(">>> ")
    if input_ != "$quit":
        print("...", main.run(input_))
    else:
        break
