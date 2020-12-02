def example(p1="", p2="222", p3="333"):
    print(p1, p2, p3)


data = {
    "p2": "BBB",
    "p3": "AAA",
}

example(**data)

example(p1="QQQ")


#---
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

numbers = [11, 22, 33]
print(my_sum(*numbers))


