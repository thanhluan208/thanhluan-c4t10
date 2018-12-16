import datetime
now = datetime.datetime.now()
print (now.hour)
while True:
    if now.hour == 16:
        print("wakeup")
        break
    else:
        print("...")