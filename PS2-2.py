# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:13:17 2019

@author: nadia
"""

# the program calculates the minimum fixed monthly payment needed 
#in order pay off a credit card balance within 12 months
#the monthly payment must be a multiple of $10 and is the same for all months

balance = 4773
annualInterestRate = 0.2

month=1
OriginalBalance=balance
MinimumFixedMonthlyPayment=10
while month<=12:
    balance = balance - MinimumFixedMonthlyPayment
    balance = balance + balance*(annualInterestRate/12)
    month+=1
    if month==13 and balance>0:
        MinimumFixedMonthlyPayment+=10
        month=1
        balance=OriginalBalance
    elif balance<=0 and month==13:
        print ('Lowest Payment: '+ str(MinimumFixedMonthlyPayment))