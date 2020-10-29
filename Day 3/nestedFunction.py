def outer(func):
    def inner():
        print("calling a function..")
        func()
        print("called a function")
    return inner

def hello():
    print("Hello")

hello = outer(hello)

hello()