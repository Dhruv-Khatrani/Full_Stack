#this is our decorator function
def my_decorator(func):
    def wrapper():
        print("before calling the function")
        func()
        print("after calling the function")

    return wrapper

@my_decorator
def dhruv():
    print("hello world")

dhruv()
