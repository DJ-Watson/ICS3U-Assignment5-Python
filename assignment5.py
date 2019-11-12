#!/usr/bin/env python3

# Created by DJ Watson
# Created on October 2019
# this program loops a number and divides it by one each time


def main():
    answer = 0
    # input
    intc = input("enter number: 1/")
    print("")

    # process and output
    try:
        numinput = int(intc)
        if numinput > 0:
            for loopn in range(numinput + 1):
                if loopn == 0:
                    continue
                else:
                    fraction = 1/loopn
                    answer += fraction
            print(answer)
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
