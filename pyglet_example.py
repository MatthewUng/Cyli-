import pyglet

class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__(600, 600)

    def on_draw(self):
        self.clear()
        pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES,
                                     [0,1,2],
                                     ('v2i', (300, 350,
                                              250, 250,
                                              350, 250)))


if __name__ == "__main__":
    window = Window()
    pyglet.app.run()
