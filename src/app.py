import sys
import os


def prime(s):
    if (s<2):
        return False
    for i in range (2,s//2+1):
        if (s%i==0):
            return False
    return True

num=int (input("Enter a number: "))
if prime (num):
    print (num, " is a Prime Number")
else:
    print (num, "is not a Prime Number")


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
