#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 23:17:32 2023

@author: YC
"""


#Write a program to calculate how many months it will take you save up enough money for a down payment. 
#LIke before, assume that your investments earn a return of ​r​ = 0.04 (or 4%) and the required down payment 
#percentage is 0.25 (or 25%). Have the user enter the following variables:


#Your program should ask the user to enter the following variables:
#1. The starting annual salary (annual_salary)
annual_salary = float(input("Enter your annual salary: "))

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

while current_savings < portion_down_payment:
    
    current_savings = current_savings * (1 + r/12) + monthly_fixed_savings
    
    number_of_months += 1
    
    if number_of_months % 6 == 0:
        monthly_fixed_savings = monthly_fixed_savings * (1 + semi_annual_raise)

print("Enter your annual salary: " + str(annual_salary))
print("Enter the percent of your salary to save, as a decimal: " + str(portion_saved))
print("Enter the cost of your dream home: " + str(total_cost))
print("Enter the semi­annual raise, as a decimal: " + str(semi_annual_raise))
print("Number of months: " + str(number_of_months))





