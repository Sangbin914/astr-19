'''
Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2PI with a thousand entries. 
Follow the basic Python program structure, including a main program function.
'''
import numpy as np


def makeTable():
    w,h = 2, 1000
    Matrix = [[0 for x in range(w)] for y in range(h)]
    val = 0
    div = np.pi / 500
    for i in range(1000):
        Matrix[i][0] = np.sin(val)
        Matrix[i][1] = val
        val += div
    return Matrix

def main():
    result = makeTable()
    print(result)

if __name__ == "__main__":
    main()


