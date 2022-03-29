#!/usr/bin/env python3

def euclidean(a, b):
    if a == 0:
        return b

    return euclidean(b % a, a)


def euclideanExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = euclideanExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def main():
    a = int(input("first number: "))
    b = int(input("Second number: "))
    print(f"gcd({a},{b}) =", euclidean(a, b))

    gcd, x, y = euclideanExtended(a, b)
    print(f"extended_euclidean({a},{b}) = {gcd}", f",{x = } ,{y = }")


if __name__ == "__main__":
    main()
