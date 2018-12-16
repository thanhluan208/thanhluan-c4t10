import pyglet

music = pyglet.resource.media("AnhDechCanGiNhieuNgoaiEm.mp3", streaming=False)
music.play()

pyglet.app.run()
