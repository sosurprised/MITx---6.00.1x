# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:20:54 2019

@author: nadia
"""
#searching for the smallest monthly payment such that we can pay off 
#the entire balance within a year; using bisection search

balance = 304070
annualInterestRate = 0.2


MonthIntRate=annualInterestRate/12
high=(balance*(1+MonthIntRate)**12)/12
low=balance/12
FixedMonthlyPayment=(high+low)/2
iter=1
OriginalBalance=balance
while iter<=12 and abs(balance)>0.1:
    balance = balance - FixedMonthlyPayment
    balance = balance + balance*MonthIntRate
    iter+=1
    if iter==13 and balance>0.1:
        low=FixedMonthlyPayment
        iter=1
        balance=OriginalBalance
    elif -0.1<balance<0.1 and iter==13:
        FixedMonthlyPayment=round(FixedMonthlyPayment, 2)
        print ('Lowest Payment: '+ str(FixedMonthlyPayment))
    elif iter==13 and balance<-0.1:
        high=FixedMonthlyPayment 
        iter=1
        balance=OriginalBalance
    FixedMonthlyPayment=(high+low)/2 
