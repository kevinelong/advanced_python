import sys


# a generator that yields items


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


n = 5
i = first_n(n)

# for x in i:
#     print(x)

# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())

print(i)

# print(sum(i))

# print(list(first_n(99)))
n = 999
print(sys.getsizeof(first_n(n)))
print(sys.getsizeof(list(first_n(n))))
