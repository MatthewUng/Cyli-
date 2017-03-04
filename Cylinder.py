import pyglet

RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Cylinder:
    def __init__(self, x, y, name):
        self.length=20
        self.name = name
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (x, y,
                                                             x, y+self.length,
                                                             x+self.length, y+self.length,
                                                             x+self.length, y)),
                                                    ('c3B', BLUE*4))

        pyglet.text.Label(str(self.name), font_name="Arial", x=x+self.length/2,
                                                             y=y+self.length/2,
                              anchor_x="center", anchor_y="center").draw()


