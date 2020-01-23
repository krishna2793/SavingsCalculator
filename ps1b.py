#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:18:18 2019

@author: ksoundar
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
portion_down_payment = 0.25 
current_savings = 0
r = 0.04 
monthly_salary = annual_salary/12
months = 0

while current_savings<(total_cost*portion_down_payment):
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved
    months += 1
    if months%6==0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12

print("Number of months: "+ str(months))