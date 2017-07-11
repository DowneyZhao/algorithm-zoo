#!/usr/bin/python3
#-*-coding: utf-8-*-
from random import random
LENGTH = 50
MAX = 99
MIN = 1

def gen(max,min,length):
    return [random()*(max-min)+min for _i in range(0,length)]

def algrithm(raw_data):
    for index in range(1,len(raw_data)):
        value = raw_data[index]
        jndex = index-1
        while(value < raw_data[jndex] and jndex>=0):
             raw_data[jndex+1] = raw_data[jndex]
             raw_data[jndex] = value
             jndex = jndex -1
    return raw_data

def main():
    target = gen(MAX,MIN,LENGTH)
    ref = []
    ref.extend(target)
    ref.sort()
    print(ref)
    result = algrithm(target)
    print(result)
    assert result == ref
    #map(lambda i: assert ref[i]==result[i],range(0,len(target))) 
if __name__ == "__main__":
    main()
