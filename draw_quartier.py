import lib.random as ra
import lib.tkinter
from preset_house import Preset


class Quartier:
    def __init__(self, min, max, seed, density, screen, color, s_chunk, s_road, s_line):

        import lib.turtle as turtle

        self.screen = screen
        self.tu = turtle.RawTurtle(self.screen)
        self.tu.setundobuffer(None)
        self.tu.speed(0)
        self.tu.hideturtle()
        self.screen.delay(0)
        # self.screen.tracer(0,0)
        ra.seed(seed)

        self.seed = seed
        self.width = int(max[0]) - int(min[0])
        self.height = int(max[1]) - int(min[1])
        self.max = max
        self.min = min

        self.s_chunk = s_chunk
        self.s_road = int(s_road)
        self.s_line = int(s_line)

        # init color
        self.color = color
        self.density = density
        # print(self.density)

        if density == "low":
            self.max_range = round(self.s_chunk * 0.025)
            self.min_range = round(self.s_chunk * 0.02)

        elif density == "middle":
            self.max_range = round(self.s_chunk * 0.035)
            self.min_range = round(self.s_chunk * 0.03)
        elif density == "water":
            self.max_range = 1
            self.min_range = 1
        else:
            self.max_range = round(self.s_chunk * 0.05)
            self.min_range = round(self.s_chunk * 0.04)

        self.calc()
        self.draw()

    def calc(self):
        # create the liste for de road position
        nb_y = ra.randint(self.min_range, self.max_range)

        self.liste = []
        for i in range(nb_y):
            nb = ra.randint(self.min_range, self.max_range)
            self.liste.append((i, nb))
        ##print("liste :",self.liste)

    def draw(self):
        # draw the road, house

        self.draw_bg(self.min[0], self.max[1])
        self.draw_road(self.s_road, self.color["road"])
        self.draw_road(self.s_line, self.color["line"])
        self.draw_house(6, self.color["house"])

    def draw_bg(self, x, y):

        self.tu.up()
        self.tu.width(2)
        self.tu.goto(x, y)
        self.tu.fillcolor(self.color["bg"])
        if self.density == "low":
            if ra.randint(0, 3) >= 1:
                self.tu.pencolor("black")
            else:
                self.tu.pencolor(self.color["bg"])

        else:
            self.tu.pencolor("black")

        self.tu.down()
        self.tu.begin_fill()
        for u in range(2):
            self.tu.forward(self.width)
            self.tu.right(90)
            self.tu.forward(self.height)
            self.tu.right(90)
        self.tu.end_fill()

    def draw_house(self, pen_width, color):
        nb = len(self.liste)

        for line in self.liste:
            if line[0] != 90:
                # print("l", line)
                for i in range(line[1]):

                    self.tu.up()
                    s = self.s_road

                    part_x = self.width // line[1]
                    part_y = self.height // (nb)

                    pos = (self.min[0] + (part_x * i), self.min[1] + (part_y * line[0]))

                    if self.density == "low":
                        i = ra.randint(0, 2)
                        if i == 0:
                            # Draw a garden
                            color = self.color["garden"]
                            pen_color = color

                        else:
                            # Draw house
                            color = self.color["house"]
                            pen_color = (color[0] - 20, color[1] - 20, color[2] - 20)

                    elif self.density == "middle":
                        i = ra.randint(0, 5)
                        if i == 0:
                            # Draw garden
                            color = self.color["garden"]
                            pen_color = color

                        else:
                            color = self.color["house"]
                            pen_color = (color[0] - 20, color[1] - 20, color[2] - 20)

                    else:
                        i = ra.randint(0, 10)
                        if i == 0:
                            color = self.color["garden"]
                            pen_color = color

                        else:
                            color = self.color["house"]
                            pen_color = (color[0] - 20, color[1] - 20, color[2] - 20)

                    # print(i, "pos :", pos)
                    self.tu.goto(pos[0], pos[1])


                    a = Preset(self.screen, self.seed, pos[0] + s, pos[1] + s, part_x - 2 * s, part_y - 2 * s, color,
                               pen_color, ra.randint(0,50))

                    del(a)
                    
    def draw_road(self, pen_width, color):

        nb = len(self.liste)
        ##print("nb road :", nb)
        if pen_width != self.s_line:
            for line in self.liste:
                if line[0] != 0:
                    self.tu.up()
                    self.tu.pencolor(color)
                    self.tu.width(pen_width)
                    self.tu.goto(self.min[0], self.min[1] + (self.height / nb) * line[0])
                    self.tu.down()
                    self.tu.seth(0)
                    self.tu.forward(self.width)

            for line in self.liste:
                for number in range(line[1]):
                    if number != line[1] - 1:
                        self.tu.up()
                        self.tu.pencolor(color)
                        self.tu.width(pen_width)
                        self.tu.goto(self.min[0] + (self.width / line[1]) * (number + 1),
                                     self.min[1] + (self.height / nb) * line[0])
                        self.tu.down()
                        self.tu.seth(90)
                        self.tu.forward((self.height / nb))
        else:
            for line in self.liste:
                if line[0] != 0:
                    self.tu.up()
                    self.tu.pencolor(color)
                    self.tu.width(pen_width)
                    self.tu.goto(self.min[0], self.min[1] + (self.height / nb) * line[0])
                    s = 0
                    while s + 20 <= self.width:
                        s += 20
                        self.tu.down()
                        self.tu.seth(0)
                        self.tu.forward(10)
                        self.tu.up()
                        self.tu.forward(10)

            for line in self.liste:
                for number in range(line[1]):
                    if number != line[1] - 1:
                        self.tu.up()
                        self.tu.pencolor(color)
                        self.tu.width(pen_width)
                        self.tu.goto(self.min[0] + (self.width / line[1]) * (number + 1),
                                     self.min[1] + (self.height / nb) * line[0])
                        s = 0

                        while s + 20 <= (self.height / nb):
                            s += 20
                            self.tu.down()
                            self.tu.seth(90)
                            self.tu.forward(10)
                            self.tu.up()
                            self.tu.forward(10)
