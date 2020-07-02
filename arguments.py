import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("-o", "--output", help="Output the result to a file", action="store_true")

parser.add_argument("num", help="The Fibonacci number you wish to calculate.", type=int)

args = parser.parse_args()

# ALL IS GOOD
result = fib(args.num)
if args.verbose:
    print("The " + str(args.num) + "th fib number is " + str(result))
elif args.quiet:
    print(result)
else:
    print("Fib(" + str(args.num) + ") = " + str(result))

if args.output:
    f = open("output.txt", "a")
    f.write(str(result) + '\n')
    f.close()
