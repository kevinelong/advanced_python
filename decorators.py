# Decorators augment a function by wrapping it which allows us to do extra work before or after the function
def the_decorator(wrapped_function):
    def wrapper():
        print("before")
        wrapped_function()
        print("after")

    return wrapper


# 1. Without Decorator Syntax
def say_hello():
    print("Hello!")
say_hello = the_decorator(say_hello)

say_hello()


# 2. With Decorator Syntax - syntactic sugar
@the_decorator
def say_goodbye():
    print("Goodbye!")


say_goodbye()
