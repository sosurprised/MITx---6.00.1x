# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:09:37 2019

@author: nadia
"""
#program that calculates the credit card balance after one year 
#if a person only pays the minimum monthly payment required by the credit
# card company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month=1
while month<=12:
    balance = balance - (balance*monthlyPaymentRate) 
    balance = balance + balance*(annualInterestRate/12)
    month+=1
    
DebtAfterYear=round(balance, 2)
print('Remaining balance after a year: ' + str(DebtAfterYear)) 
