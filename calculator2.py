#!/usr/bin/env python3
import sys

def translateToDict(str_):
    try:
        key,value = str_.split(':')
        value = int(value)
        dict1[key] = value
    except ValueError:
        print("paramater error")
    
    t =value -value*(0.08+0.02+0.005+0.06) - 5000
    s =value -value*(0.08+0.02+0.005+0.06)
    if t<=0:
        dict1[key] = s
    if t>0 and t<=3000:
        dict1[key] = s - t*0.03
    if t>3000 and t<=12000:
        dict1[key] = s - t*0.1 +210
    if t>12000 and t<=25000:
        dict1[key] = s - t*0.2 +1410
    if t>25000 and t<=35000:
        dict1[key] = s - t*0.25+2660
    if t>35000 and t<=55000:
        dict1[key] = s - t*0.3+4410
    if t>55000 and t<=80000:
        dict1[key] = s - t*0.35+7160
    if t>80000:
        dict1[key] = s - t*0.45+15160
    
    print("{}:{:.2f}".format(key,dict1[key]))

if __name__ == '__main__':
    global dict1
    dict1 = {}
    for arg in sys.argv[1:]: 
        translateToDict(arg)

