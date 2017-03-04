import pyglet
from Cylinder import Cylinder

WHITE = (255, 255, 255)
LIGHT_GREY = (170, 170, 170)
GREY = (100, 100, 100)
DARK_GREY = (25, 25, 25)
BLACK = (0, 0, 0)

class GameBoard(pyglet.window.Window):

    def __init__(self, length=600):
        super(GameBoard, self).__init__(length, length)
        self.length = length


    def on_draw(self):

        top_color = GREY + WHITE + WHITE + GREY
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (0, self.length*2/3,
                                                             0, self.length,
                                                             self.length, self.length,
                                                             self.length, self.length*2/3)),
                                                    ('c3B', top_color))

        bottom_color = BLACK + DARK_GREY + DARK_GREY + BLACK
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (0, 0,
                                                             0, 400,
                                                             600, 400,
                                                             600, 0)),
                                                    ('c3b', bottom_color))

        pyglet.text.Label("Fast", font_name="Arial", font_size=16, x=10, y=self.length*2/3+5).draw()
        pyglet.text.Label("Slow", font_name="Arial", font_size=16, x=10, y=self.length*2/3-25).draw()

        temp = Cylinder(100, 100, 0)

        print "drawing complete"

if __name__ == "__main__":
    g = GameBoard()
    pyglet.app.run()
    print "after running"