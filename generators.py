import sys


# a generator that yields items


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


n = 1000000
i = first_n(n)

print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())

print(sum(first_n(n)))
print(list(first_n(n)))

print(sys.getsizeof(first_n(n)))
print(sys.getsizeof(list(first_n(n))))
