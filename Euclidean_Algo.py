#!/usr/bin/env python3

def euclidean(a, b):
    # keep dividing until the reminder is 0
    if a == 0:
        return b
    
    # get the reminder (smaller number) until 
    return euclidean(b % a, a)


def main():
    a = int(input("first number: "))
    b = int(input("Second number: "))
    
    print(f"gcd({a},{b}) =", euclidean(a, b))


if __name__ == "__main__":
    main()
