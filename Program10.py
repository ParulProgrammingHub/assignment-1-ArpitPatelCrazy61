def simple_interest(principal,time,rate):
    simpleinterestvalue = (principal * rate * time) / 100
    return simpleinterestvalue

principal = input("enter principal amount : ")
rate = input("enter rate percentage : ")
time = input("enter time : ")

c = simple_interest(principal,time,rate)
print("your simple interest is {}".format(c))









