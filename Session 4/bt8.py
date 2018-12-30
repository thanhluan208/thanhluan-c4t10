import datetime
import pyglet
while True:
    now = datetime.datetime.now()
    print(now)
    if now.second == 16:
        music = pyglet.resource.media("Con-Trai-Cung-K-ICM-B-Ray.mp3")
        music.play()
        pyglet.app.run()
        break
    else:
        print("...")