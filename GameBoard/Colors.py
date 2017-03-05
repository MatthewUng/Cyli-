WHITE = (255, 255, 255)
LIGHT_GREY = (170, 170, 170)
GREY = (100, 100, 100)
DARK_GREY = (25, 25, 25)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
COLOR_GRADIENT = [(0+((255/10)*i), 0, 255-((255/10)*i)) for i in range(11)]

def index_to_color(n):
    return COLOR_GRADIENT[n]