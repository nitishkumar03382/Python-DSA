# LINK: 
# https://www.codingninjas.com/studio/problems/two-stacks_983634
from os import *
from sys import *
from collections import *
from math import *

# Complete this class
class TwoStack:
    
    def __init__(self, s):
        self.arr = [None] * s
        self.top1 = -1
        self.top2 = s

    # Push function for the first stack
    def push1(self, val):
        if self.top2 - self.top1 > 1:
            self.top1 += 1
            self.arr[self.top1] = val
        else:
            return -1
            

    # Push function for the second stack
    def push2(self, val):
        if self.top2 - self.top1 > 1:
            self.top2 -= 1
            self.arr[self.top2] = val
        else:
            return -1

    # Pop function for the first stack
    def pop1(self):
        if self.top1 == -1:
            return -1
        else:
            ele = self.arr[self.top1]
            self.top1 -= 1
            return ele


    # Pop function for the second stack
    def pop2(self):
        if self.top2 == len(self.arr):
            return -1
        else:
            ele = self.arr[self.top2]
            self.top2 += 1
            return ele
