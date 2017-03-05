import csv
from GameBoard.GameBoard import GameBoard
from GameBoard.Colors import index_to_color
import sys
import random
import pyglet
import time


variance = 1
# each element in days is a day
# each day contains [cylinder, rate]
days = list()
all = range(10)


fast = list()
slow = list()

def parse_csv(f):
    with open(f, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',',)
        count = -1
        for row in reader:
            if len(row) == 3 and int(row[2]) != count:
                days.append(dict())
                days[-1][int(row[0])] = int(row[1])
                count += 1

            elif len(row) == 3:
                days[-1][int(row[0])] = int(row[1])
            else:
                continue
    print "done parsing"

def random_init(n):
    """picks n random cylinders from all"""
    temp = all[:]
    out = list()
    for _ in range(n):
        out.append(random.choice(temp))
        temp.remove(out[-1])
    return out, temp


def mutation(fast, slow):
    fast = fast[:]
    slow = slow[:]
    def swap(i, j):
        """swaps i from fast with j from slow"""
        temp = fast[i]
        fast[i] = slow[j]
        slow[j] = temp

    for _ in range(variance):
        i = random.choice(range(len(fast)))
        j = random.choice(range(len(slow)))
        swap(i, j)
    return fast, slow


def get_colors(fast, slow, day_i):
    """returns the colors list for a particular day"""
    day = days[day_i]
    out = []
    for i in fast:
        out.append(day[i])
    for i in slow:
        out.append(day[i])
    return out

def run_test(fast, slow):
    print "trial with ", fast, slow
    names = fast+slow
    colors = get_colors(fast, slow, 0)
    color_tup = map(index_to_color, colors)

    fitness_score = 0
    day = 0
    g = GameBoard(len(all), len(fast), names, color_tup)
    g.set_date("Day: {}".format(day))

    for i in range(1, 360):
        pyglet.clock.tick()

        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_events()
            window.dispatch_event('on_draw')
            window.flip()

        for name in names:
            index = names.index(name)
            colors_day = get_colors(fast, slow, i)
            if name in fast:
                temp = (colors_day[name] - 5)
                fitness_score += temp
            else:
                continue
                #fitness_score += -1*colors[index]+5

        day += 1
        g.update_color(days[day])
        g.set_date("Day: {}".format(day))
        g.set_score(fitness_score)
        time.sleep(0.001)
    g.close()
    print "score of:", fitness_score
    return fitness_score

def perform_tests(n):
    best_score = -sys.maxint
    first, last = None, None
    pot_first, pot_last = random_init(2)

    for i in range(n):
        print "\ntest:", i+1

        score = run_test(pot_first, pot_last)
        print best_score, score
        if score > best_score:
            print "here"
            first, last = pot_first, pot_last
            best_score = score

        print first, last
        print pot_first, pot_last
        pot_first, pot_last = mutation(first, last)


        print "after"
        print first, last
        print pot_first, pot_last


    print "best score: ", best_score
    print first, last




if __name__ == "__main__":
    parse_csv('history.txt')
    print all
    perform_tests(20)
