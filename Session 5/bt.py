import time
def countdown(t):
    while t > 0:
        print (t)
        t = t - 1
        if t == 0:
            print("hello")
countdown(50)