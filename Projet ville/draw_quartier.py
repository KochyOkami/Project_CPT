import lib.random as ra
import lib.tkinter

class Quartier:
    def __init__(self, min, max, seed, density, screen, c_bg, c_house, c_road, c_line,s_chunk, s_road, s_line):

        import lib.turtle as turtle
        
        self.screen = screen
        self.tu = turtle.RawTurtle(self.screen)
        self.tu.setundobuffer(None)
        self.tu.speed(0)
        self.tu.hideturtle()
        self.screen.delay(0)
        #self.screen.tracer(0,0)
        ra.seed(seed)
        
        self.seed= seed
        self.width = int(max[0]) - int(min[0])
        self.height = int(max[1]) - int(min[1])
        self.max = max
        self.min = min
        
        self.s_chunk = s_chunk
        self.s_road = int(s_road)
        self.s_line = int(s_line)
        
         #init color
        self.c_bg = c_bg
        self.c_road = c_road
        self.c_line = c_line
        self.c_house = (int(c_house[0]), int(c_house[1]), int(c_house[2]),)
        self.density = density
        #print(self.density)
        
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
        #create the liste for de road position 
        nb_y = ra.randint(self.min_range, self.max_range)
        
        self.liste = []
        for i in range(nb_y):
            nb = ra.randint(self.min_range, self.max_range)
            self.liste.append((i, nb))
        ##print("liste :",self.liste)
        

    def draw(self):
        #draw the road, house
        
        self.draw_bg(self.min[0], self.max[1])
        self.draw_road(self.s_road, self.c_road)
        self.draw_road(self.s_line, self.c_line)
        self.draw_house(6,self.c_house)
        
    def draw_bg(self, x, y):
        
        self.tu.up()
        self.tu.width(2)
        self.tu.goto(x,y)
        self.tu.fillcolor(self.c_bg)
        if ra.randint(0,3) >= 1:self.tu.pencolor("black")
        else:self.tu.pencolor(self.c_bg)
        self.tu.down()
        self.tu.begin_fill()
        for u in range(2):
            self.tu.forward(self.width)
            self.tu.right(90)
            self.tu.forward(self.height)
            self.tu.right(90)
        self.tu.end_fill()
       
        
    def draw_house(self, pen_width, pen_color):
        nb = len(self.liste)
        s = self.s_road
        for line in self.liste:
            if line[0] != 90:
                #print("l", line)
                for i in range(line[1]):
                          
                    self.tu.up()
                    part_x = self.width//line[1]
                    part_y = self.height//(nb)
                    
                    pos = (self.min[0] + (part_x * i) + s, self.min[1]+ (part_y* line[0]) + s)
                    
                    w_house = part_x- s*2
                    h_house = part_y - s*2
                    border_x =(2*pos[0] - w_house)/ ra.uniform(1.2, 2.0)
                    border_y =(2*pos[1] -h_house) /ra.uniform(1.2, 2.0)
                    
                    if self.density == "low":
                        i = ra.randint(0,2)
                        j = ra.randint(0,30)
                        if i == 0:
                            pen_color = (206,230,214)
                            state = 0
                        
                        elif j == 0:
                            pen_color = (0,100, ra.randint(200, 250))
                            state = 0
                        else:
                            p = 5
                            pen_color =  (ra.randint(int(self.c_house[0]), int(self.c_house[0]) + p), ra.randint(int(self.c_house[1]), int(self.c_house[1]) + p), ra.randint(int(self.c_house[2]), int(self.c_house[2]) + p))
                            state = 1
                            
                    elif self.density == "middle":
                        i = ra.randint(0,5)
                        if i == 0:
                            pen_color = (206,230,214)
                            state = 0
                        else:
                            pen_color =  (ra.randint(int(self.c_house[0]), int(self.c_house[0]) + 5), ra.randint(int(self.c_house[1]), int(self.c_house[1]) + 5), ra.randint(int(self.c_house[2]), int(self.c_house[2]) + 5))
                            state = 1
                      
                    else:
                        i = ra.randint(0,10)
                        if i == 0:
                            pen_color = (206,230,214)
                            state = 0
                        else:
                            pen_color =  (ra.randint(int(self.c_house[0]), int(self.c_house[0]) + 5), ra.randint(int(self.c_house[1]), int(self.c_house[1]) + 5), ra.randint(int(self.c_house[2]), int(self.c_house[2]) + 5))
                            state = 1
                           
                     
            
            
                    ##print(i, "pos :", pos)
                    self.tu.goto(pos[0] , pos[1])
                    c_house = self.c_house
                    
                        

                    from preset_house import Preset
                    
                    if state:
                        if ra.randint(0,3) != 0:
                            a = Preset(self.screen, self.seed, pos[0], pos[1], w_house, h_house, pen_color)
                            del(a)
                        else:
                            state = not state
                            
                    if not state:
                        self.tu.goto(pos[0] + 2 , pos[1] + 2)
                        self.tu.width(1)
                        self.tu.pencolor((203,203,201))
                        self.tu.width(1)
                        self.tu.fillcolor(pen_color)
                        self.tu.down()
                        self.tu.begin_fill()
                        self.tu.seth(90)
                        for _ in range(2):
                            
                            self.tu.forward(h_house -2)
                            self.tu.right(90)
                            self.tu.forward(w_house-2)
                            self.tu.right(90)
                        self.tu.end_fill()
                
        
    def draw_road(self,pen_width, pen_color):
        
        nb = len(self.liste)
        ##print("nb road :", nb)
        if pen_width != self.s_line:
            for line in self.liste:
                if line[0] != 0:
                    self.tu.up()
                    self.tu.pencolor(pen_color)
                    self.tu.width(pen_width)
                    self.tu.goto(self.min[0] ,self.min[1] + (self.height/nb) *line[0])
                    self.tu.down()
                    self.tu.seth(0)
                    self.tu.forward(self.width)
                    
            for line in self.liste:
                for number in range(line[1]):
                    if number != line[1]-1:
                        self.tu.up()
                        self.tu.pencolor(pen_color)
                        self.tu.width(pen_width)
                        self.tu.goto(self.min[0] + (self.width/line[1]) * (number + 1), self.min[1] + (self.height/nb) * line[0])
                        self.tu.down()
                        self.tu.seth(90)
                        self.tu.forward((self.height/nb))
        else:
            for line in self.liste:
                if line[0] != 0:
                    self.tu.up()
                    self.tu.pencolor(pen_color)
                    self.tu.width(pen_width)
                    self.tu.goto(self.min[0], self.min[1] + (self.height/nb) *line[0])
                    s = 0
                    while s +20 <= self.width:
                        s += 20
                        self.tu.down()
                        self.tu.seth(0)
                        self.tu.forward(10)
                        self.tu.up()
                        self.tu.forward(10)
                    
            for line in self.liste:
                for number in range(line[1]):
                    if number != line[1]-1:
                        self.tu.up()
                        self.tu.pencolor(pen_color)
                        self.tu.width(pen_width)
                        self.tu.goto(self.min[0] + (self.width/line[1]) * (number + 1),self.min[1] + (self.height/nb) * line[0])
                        s = 0

                        while s + 20 <= (self.height/nb):
                            s += 20
                            self.tu.down()
                            self.tu.seth(90)
                            self.tu.forward(10)
                            self.tu.up()
                            self.tu.forward(10)

