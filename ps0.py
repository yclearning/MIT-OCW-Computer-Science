#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:05:20 2023

@author: YC
"""

import math
#Write a program that does the following in order:
    
#1. Asks the user to enter a number “x” 

x_input = input("Enter a number x: ")

x = float(x_input)

#2. Asks the user to enter a number “y”

y_input = input("Enter a number y: ")

y = float(y_input)

#3. Prints out number “x”, raised to the power “y”. 

print(x)
x**y

#4. Prints out the log (base 2) of “x”.

log_x = math.log2(x)

print(log_x)
