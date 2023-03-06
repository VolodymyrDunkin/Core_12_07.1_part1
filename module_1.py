from ex_01 import greeting
from normalize import normalize

def take_name():
    user_input = input('Type your name >>>')
    return normalize(user_input)


if __name__ == "__main__":

    result = greeting(take_name())

    print(result)