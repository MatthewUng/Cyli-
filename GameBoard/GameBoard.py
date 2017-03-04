import pyglet
from UI_Cylinder import UI_Cylinder
from Colors import *
import random

class GameBoard(pyglet.window.Window):

    def __init__(self, num, numFast, colors, length=600):
        super(GameBoard, self).__init__(length, length)
        self.length = length
        self.num = num
        self.numFast = numFast
        self.cylinders = list()
        self.score = 0
        self.score_label = None
        self.date_label = None
        self.date = None
        self.colors = colors

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


        self.update_score(0)
        self._init_rectangles(self.colors)

    def update_date(self, date):
        pyglet.graphics.draw(4,
                             pyglet.gl.GL_QUADS,
                             ('v2i', (0, self.length - 22,
                                      0, self.length,
                                      self.length, self.length,
                                      self.length, self.length - 22)),
                             ('c3B', WHITE * 4))
        self.score_label.draw()
        self.date = date
        self.date_label = pyglet.text.Label(date,
                                          font_name="Arial",
                                          font_size=16,
                                          x=self.length,
                                          y=self.length-20,
                                          anchor_x='right')
        self.date_label.set_style('color', (0, 0, 0, 255))
        self.date_label.draw()

    def _init_rectangles(self, colors):

        max_per_row = 1
        while max_per_row*30 < self.length-200:
            max_per_row += 1

        row_width = 30 * max_per_row
        center = self.length/2

        fast_rows = (self.numFast / max_per_row)
        if self.numFast % max_per_row:
            fast_rows += 1

        slow_rows = (self.num - self.numFast) / max_per_row
        if (self.num - self.numFast) % max_per_row:
            slow_rows += 1

        #print "fast, slow rows", fast_rows, slow_rows

        top = self.length - 22
        middle = self.length * 2 /3
        bottom = 0

        #print "top, middle, top", top, middle, bottom

        top_diff = (top-middle) / fast_rows
        bottom_diff = (middle-bottom) / slow_rows

        #print "top_diff, bottom_diff", top_diff, bottom_diff

        if top_diff < 30 or bottom_diff < 30:
            print "error in creating board\nboard is too small"

        for i in range(self.num):
            if i < self.numFast:
                curr_row = i / max_per_row + 1

                x = center - row_width/2 + 30*(i%max_per_row)
                y = middle + (top_diff * curr_row) / 2 - 15
                temp = UI_Cylinder(x, y, i, colors[i])
                self.cylinders.append(temp)
            else:

                k = i - self.numFast
                curr_row = k / max_per_row + 1
                x = center -row_width/2 + 30*(k%max_per_row)
                y = bottom + (bottom_diff * curr_row) /2 -15

                temp = UI_Cylinder(x, y, i, colors[i])
                self.cylinders.append(temp)

        self.swap(0, 10)

    def update_score(self, score):
        pyglet.graphics.draw(4,
                             pyglet.gl.GL_QUADS,
                             ('v2i', (0, self.length -22,
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
        if self.date_label:
            self.date_label.draw()

    def swap(self, i, j):
        i_name, i_color = self.cylinders[i].get_attributes()
        j_name, j_color = self.cylinders[j].get_attributes()
        self.cylinders[i].change_color_name(j_color, j_name)
        self.cylinders[j].change_color_name(i_color, i_name)

if __name__ == "__main__":
    colors = list()
    colors.append(RED)
    for _ in range(19):
        colors.append(BLUE)

    #colors = [random.choice(COLOR_GRADIENT) for _ in range(50)]
    g = GameBoard(20, 10, colors)
    pyglet.app.run()
    print "fml"
