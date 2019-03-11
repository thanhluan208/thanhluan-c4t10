from __future__ import unicode_literals
import youtube_dl
import pyglet

import json
from youtube_dl import YoutubeDL
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


print("Hello this is TK music app")
iid = []
durations = []
duration = []
creators = []
creator = []
songgs = []
idd = []
hhh = []
songs = []
detail = {}
aa = ["Show All Song", "Show detail of a song", "Play a song","Search and download songs","Exit"]
for i, d in enumerate(aa):
    print(i + 1,d)
b = int(input("Pick one of these number:"))
while True:
    aa = ["Show All Song", "Show detail of a song", "Play a song","Search and download songs","Exit"]
    for i, d in enumerate(aa):
        print(i + 1,d)
    b = int(input("Pick one of these number:"))
    
    if b == 4:
        c = input("Song's name:")
        
        options = {
        'default_search': 'ytsearch5'
        }

        ydl = YoutubeDL(options)
        search_result = ydl.extract_info(c, False)
        a = search_result["entries"]
        for e in range(5):
            p = a[e]
            duration.append(p["duration"])
            creator.append(p["creator"])
            idd.append(p["display_id"])
            songs.append(p["title"])
        for g in range(0,5):
            h = a[g]
            hhh.append(h["webpage_url"])
        # for xx,zz in enumerate(hhh):
        #     print(xx,zz)
        for x,z in enumerate(songs):
            print(x,z)
        quest = int(input("pick one number to download"))
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([hhh[quest]])
        quest1 = input("Do you want to play now?")
        if quest1 == "yes":
            # đoạn này bị lỗi
            sumss = songs[quest]+ "-" +  idd[quest] + ".mp3"
            source = pyglet.load(sumss)
            player = Player()
            player.queue(source)
            player.play()
            disc = "on"
            while disc == "on":
                quest2 = input("choose pause, continue, stop:")
                if quest2 == "pause":
                    player.stop()
                elif quest2 == "stop":
                    player.delete()
                    break
                elif quest2 == "continue":
                    player.play()
            pyglet.app.run()
        else:
            durations.append(duration[quest])
            creators.append(creator[quest])
            iid.append(idd[quest])
            songgs.append(songs[quest])
    if b == 1:
        if songgs == []:
            print("song list is empty")
        else:
            print(songgs)
    if b == 3:
        if songgs == []:
            print("song list is empty")
        else:
            for xx, yy in enumerate(songgs):
                print(xx,yy)
            xy = int(input("pick one number to play:"))
            sumss = songgs[quest]+ "-" +  idd[quest] + ".mp3"
            music = pyglet.resource.media(sumss)
            music.play()
            pyglet.app.run()
    if b == 2:
        for xx,yy in enumerate(songgs):
            print(xx,yy)
        yx = int(input("pick one number to show detail"))
        print("ID:",*idd)
        print("TITLE:", *songgs)
        print("DURATION:", *durations)
        print("Creator:", *creators )
        xyz = input("press any key to continue...")
    if b == 5:
        break   