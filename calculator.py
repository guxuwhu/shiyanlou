#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Parameter Error")
        sys.exit()
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
        sys.exit() #遇到异常时不执行后面的程序
    s = num - 5000
    if s <=0:
        sum = 0
    elif s <= 3000:
        sum = s*0.03
    elif s > 3000 and s <=12000:
        sum = s*0.1 - 210
    elif s >12000 and s <=25000:
        sum = s*0.2 - 1410
    elif s > 25000 and s <= 35000:
        sum = s*0.25 - 2660
    elif s > 35000 and s <55000:
        sum = s*0.3 -4410
    elif s >55000 and s <80000:
        sum = s*0.35 -7160
    else:
        sum = s*0.45-15160
    print("{:.2f}".format(sum))

