from __future__ import division
def compound_interest(principle,rate,time):
    x = ( 1 + (rate / 100))**time
    compoundinterestvalue = (principle * x - principle )
    return compoundinterestvalue

principle = input("enter principle amount : ")
rate = input("enter rate : ")
time = input("enter time :")

c = compound_interest(principle,rate,time)
print("your compound interest is {}".format(c))







