import pyglet

WHITE = (255, 255, 255)
LIGHT_GREY = (170, 170, 170)
GREY = (100, 100, 100)
DARK_GREY = (25, 25, 25)
BLACK = (0, 0, 0)

class GameBoard(pyglet.window.Window):

    def __init__(self):
        super(GameBoard, self).__init__(600, 600)


    def on_draw(self):

        top_color = GREY + WHITE + WHITE + GREY
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (0, 400,
                                                             0, 600,
                                                             600, 600,
                                                             600, 400)),
                                                    ('c3B', top_color))

        bottom_color = BLACK + DARK_GREY + DARK_GREY + BLACK
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (0, 0,
                                                             0, 400,
                                                             600, 400,
                                                             600, 0)),
                                                    ('c3b', bottom_color))

        pyglet.text.Label("Fast", font_name="Arial", font_size=16, x=30, y=420, anchor_x="center", anchor_y="center").draw()
        pyglet.text.Label("Slow", font_name="Arial", font_size=16, x=33, y=380, anchor_x="center", anchor_y="center").draw()

        print "drawing complete"

if __name__ == "__main__":
    g = GameBoard()
    pyglet.app.run()
    print "after running"