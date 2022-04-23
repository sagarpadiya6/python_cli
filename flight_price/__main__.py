#!/usr/bin/env python

import sys
from .flight_price import predict


def main():
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    predict()


if __name__ == '__main__':
    main()
