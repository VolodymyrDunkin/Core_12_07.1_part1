def greeting(name):
    return f"Hello {name}"


def greeting2():
    return f"Hello from greeting2"

def greeting3():
    return f"Hello from greeting3"

def greeting4():
    return f"Hello Hello from greeting4"


print(greeting2())
print(greeting3())
print(greeting4())

if __name__ == "__main__":
    print(greeting('Bill'))