import pyglet

class UI_Cylinder:
    def __init__(self, x, y, name, color):
        print color
        self.length=20
        self.name = name
        self.color = color
        self.vertex = pyglet.graphics.vertex_list(4, ('v2i', (x, y,
                                                      x, y+self.length,
                                                      x+self.length, y+self.length,

                                                      x+self.length, y)),
                                                     ('c3B', color*4))

        self.vertex.draw(pyglet.gl.GL_QUADS)

        self.label = pyglet.text.Label(str(self.name),
                                       font_name="Arial",
                                       x=x+self.length/2,
                                       y=y+self.length/2,
                                       anchor_x="center",
                                       anchor_y="center")
        self.label.draw()

    def get_attributes(self):
        return self.name, self.color

    def change_color(self, color):
        self.vertex.colors[:] = color*4
        self.vertex.draw(pyglet.gl.GL_QUADS)
        self.label.draw()

    def change_name(self, name):
        self.vertex.draw(pyglet.gl.GL_QUADS)
        self.label.text = str(name)
        self.label.draw()

    def change_color_name(self, color, name):
        self.vertex.colors[:] = color*4
        self.vertex.draw(pyglet.gl.GL_QUADS)
        self.label.text = str(name)
        self.label.draw()