#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 23:17:32 2023

@author: YC
"""


#In​ ps1c.py​, write a program to calculate the best savings rate, as a function of your starting salary. 
#You should use ​bisection search​ to help you do this efficiently. You should keep track of the number of 
#steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote for part B in this problem.


#Your program should ask the user to enter the following variables:
#1. The starting annual salary (annual_salary)
annual_salary = float(input("Enter your starting salary: "))

#2. The portion of salary to be saved (portion_saved)
portion_saved = float(input("Enter your portion of salary to be saved: "))

#3. The cost of your dream home (total_cost)
total_cost = float(input("Enter the cost of your dream home: "))

#4. The semi­annual salary raise (semi_annual_raise)
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))


r = 0.04

portion_down_payment = 0.25 * total_cost

current_savings = 0

monthly_fixed_savings = annual_salary * portion_saved / 12

number_of_months = 0

best_saving_rate = 0

steps_in_bisection_search = 0

while current_savings < portion_down_payment:
    
    current_savings = current_savings * (1 + r/12) + monthly_fixed_savings
    
    number_of_months += 1
    
    if number_of_months % 6 == 0:
        monthly_fixed_savings = monthly_fixed_savings * (1 + semi_annual_raise)
        
        
    
        
    steps_in_bisection_search += 1



print("Enter your starting salary: " + str(annual_salary))
print("Best savings rate:​ " + str(best_saving_rate))
print("Steps in bisection search: " + str(steps_in_bisection_search))





