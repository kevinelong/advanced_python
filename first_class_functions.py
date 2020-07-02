def greet(message):
    print(message)


# Anonymous function AKA lambda
greet2 = lambda message: print(message)

greet("Hello there!!!")
greet2("Hi.")

identifier3 = greet

identifier3("Whats up?")

a = 3
b = a
print(b)


def outer(message):
    my_message = message

    def inner():
        print(my_message)

    return inner


func = outer("Hello!!!!")

func()
func()
func()
func()
