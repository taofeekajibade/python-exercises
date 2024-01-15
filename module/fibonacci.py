def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


""" the code below allows the module to be
capable of being run as a script from the command line.
"""
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    print("I am being run directly.")
else:
    print("I am being imported.")
