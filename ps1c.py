#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:18:18 2019

@author: ksoundar
"""
starting_salary = annual_salary = float(input("Enter the starting salary: "))
portion_saved = 1
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 
current_savings = 0
monthly_salary = annual_salary/12
minrate = 0
maxrate = 10000
months = 36
r = 0.04

def monthsTaken(total_cost, current_savings, portion_down_payment, semi_annual_raise, annual_salary, portion_saved, r):
    months = 0
    monthly_salary = annual_salary/12
    while current_savings<(total_cost*portion_down_payment):
        current_savings += current_savings*r/12
        current_savings += monthly_salary*portion_saved
        months += 1
        if months%6==0:
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary = annual_salary/12
    return months,current_savings

def rateSearch(minrate, maxrate, months):
    mid = int((maxrate-minrate)/2) + minrate
    portion_saved = float(mid)/10000
    monthsCalculated, saving = monthsTaken(total_cost, current_savings, portion_down_payment, semi_annual_raise, annual_salary, portion_saved, r)
    if months == monthsCalculated:
        if saving-(total_cost*portion_down_payment)<100:
            return portion_saved,1
        else:
            portion_saved, steps = rateSearch(minrate, mid, months)
            return portion_saved, steps+1
    elif months<monthsCalculated:
        portion_saved, steps = rateSearch(mid, maxrate, months)
        return portion_saved, steps+1
    else:
        portion_saved, steps = rateSearch(minrate, mid, months)
        return portion_saved, steps+1
 
monthsCalculated, saving = monthsTaken(total_cost, current_savings, portion_down_payment, semi_annual_raise, annual_salary, portion_saved, r)       
if monthsCalculated>months:
    print("It is not possible to pay the down payment in three years.")
else:
    portion_saved, steps = rateSearch(minrate, maxrate, months)
    print("Best savings rate: "+ str(portion_saved))
    print("Steps in bisection search: "+ str(steps))