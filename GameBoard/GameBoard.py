import pyglet
from UI_Cylinder import UI_Cylinder

WHITE = (255, 255, 255)
LIGHT_GREY = (170, 170, 170)
GREY = (100, 100, 100)
DARK_GREY = (25, 25, 25)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
BLUE = (0, 0, 255)

class GameBoard(pyglet.window.Window):

    def __init__(self, num, numFast, length=600):
        super(GameBoard, self).__init__(length, length)
        self.length = length
        self.num = num
        self.numFast = numFast
        self.score = 0

    def on_draw(self):

        top_color = GREY + WHITE + WHITE + GREY
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (0, self.length*2/3,
                                                             0, self.length,
                                                             self.length, self.length,
                                                             self.length, self.length*2/3)),
                                                    ('c3B', top_color))

        bottom_color = BLACK + DARK_GREY + DARK_GREY + BLACK
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (0, 0,
                                                             0, self.length*2/3,
                                                             self.length, self.length*2/3,
                                                             self.length, 0)),
                                                    ('c3b', bottom_color))

        pyglet.text.Label("Fast", font_name="Arial", font_size=16, x=10, y=self.length*2/3+5).draw()
        pyglet.text.Label("Slow", font_name="Arial", font_size=16, x=10, y=self.length*2/3-25).draw()


        self.score = None

        self.update_score(0)

        temp = UI_Cylinder(100, 100, 0, BLUE)
        temp.change_color_name(RED, '2')

        print "drawing complete"

    def _init_rectangles(self, num, colors):
        pass

    def update_score(self, score):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (0, self.length -22,
                                                             0, self.length,
                                                             self.length, self.length,
                                                             self.length, self.length-22)),
                                                    ('c3B', WHITE*4))
        self.score = score
        self.score_label = pyglet.text.Label("Score: {}".format(self.score),
                                             font_size=16,
                                             x=10,
                                             y=self.length-20)
        self.score_label.set_style('color', (0, 0, 0, 255))
        self.score_label.draw()


if __name__ == "__main__":
    g = GameBoard(6 ,3)
    pyglet.app.run()

    print "after running"