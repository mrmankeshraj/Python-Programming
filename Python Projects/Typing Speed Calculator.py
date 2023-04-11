"""
"""

from time import *
import random as r

def mistake(partest, usertest):
    error = 0

    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput)/ time_r
    return round(speed)

test = ["It's not who you are inside it's what you do that defines you.", "My name is Mankesh Raj.", "Welcome to my channel."]

test1 = r.choice(test)

print("*****Typing Speed******")
print(test1)
print()
print()

time_1 = time()
testinput = input("Enter : ")
time_2 = time()

print("speed : ", speed_time(time_1, time_2, testinput), "w/sec")
print("Error : ", mistake(test1, testinput))