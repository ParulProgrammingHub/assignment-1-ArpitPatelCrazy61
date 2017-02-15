from __future__ import division
print("marks obtained in five subjects : ")
m1 = input()
m2 = input()
m3 = input()
m4 = input()
m5 = input()

mean = (m1 + m2 + m3 + m4 + m5) / 5
percentage = (m1 + m2 + m3 + m4 + m5) / 500 * 100
print(percentage)
print("your percentage is {0}".format(percentage))
if percentage < 35:
    print("you are fali :( ")
else:
    print("you ara pass :) ")
