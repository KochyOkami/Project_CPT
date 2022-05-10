import lib.random as ra
class Generate_town:
    
    def __init__(self,settings):
        
        import lib.tkinter as tkinter
        import lib.turtle as turtle
        
        
        #Settings of the size
        self.width = settings["width"]
        self.height = settings["height"]
        self.s_chunk = settings["size_chunk"]
        self.seed = settings["seed"]
        self.s_road = settings["size_road"]
        self.s_line = settings["size_line"]
        self.liste_hight = []
        self.coord = []
        self.min = []
        
        #Settings of the color
        self.c_bg = settings["color_bg"]
        self.c_house = settings["color_house"]
        self.c_road = settings["color_road"]
        self.c_line = settings["color_line"]
        self.c_text = settings["color_text"]
        
        #Other settings
        ra.seed(self.seed)
        self.show_perlin = settings["show_noise"]
        self.style = ('Courier', 40, 'bold')
        self.save = settings["save"]
        self.debug_mode = bool(settings["debug_mode"])
        self.settings = settings
        self.octaves = int(settings["octaves"])
        
        #create the window
        map = tkinter.Tk()
        map.title("Carte " + str(self.seed))
        map.iconbitmap("img/logo/logo.ico")
        map.geometry(str(settings["width_map"]) + "x" + str(settings["height_map"]))
        
        #Create the canvas for draw all compnantes
        self.canvas = tkinter.Canvas(map,width = self.width, height = self.height)
        
        #Crete scrollbar for the window
        hbar=tkinter.Scrollbar(map, orient=tkinter.HORIZONTAL)
        hbar.pack(side=tkinter.BOTTOM,fill=tkinter.X)
        hbar.config(command=self.canvas.xview)
        
        vbar=tkinter.Scrollbar(map,orient=tkinter.VERTICAL)
        vbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        vbar.config(command=self.canvas.yview)
        
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack()
        

        #initial value for turtle 
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.colormode(255)
        self.tu = turtle.RawTurtle(self.screen)
        
        self.tu.setundobuffer(None)
        self.tu.speed(0)
        self.tu.hideturtle()
        self.screen.delay(0)
        self.screen.tracer(0,0)
        self.screen.setworldcoordinates(0, self.height, self.width, 0)
        
        #draw the map        
        self.draw()
        self.update()
        
        #draw cartouche
        photo = tkinter.PhotoImage(file = "img/logo/logo64.gif", master=map)
        self.canvas.create_rectangle(31,settings["height"] - 75, settings["width"] -31, settings["height"] - 11, fill="#FFFFFF")
        self.canvas.create_text(settings["width"]//2, settings["height"] - 40, text= "Carte vu du ciel " + str(settings["width"]) + "x" + str(settings["height"]), anchor = tkinter.CENTER)
        self.canvas.create_text(settings["width"] - 100, settings["height"] - 40, text = "©CPTcorporation", font = "Ariel 5")
        i = self.canvas.create_image(66, settings["height"] - 42 , image=photo)
        map.mainloop()
        
        #Save the map in .eps format
        if self.save:
            print("Saved")
            self.canvas.postscript(file = "save/seed " + str(self.seed) + ".eps", colormode = 'color', height = self.height, width = self.width)
            print(self.coord)
        
        
    def update(self):
        '''Update the canvas.'''
        self.screen.update()
 
 
    def color(self):
        '''Attribute the differente density for the map.'''
        
        #select the range for the perlin noise
        noise_value = self.perlin()
         
        noise = []
        for row in noise_value:
            line = []
            for value in row:
                 
                
                if value < -0.2:
                    line.append("hight")
                    
                elif -0.2 <= value < 0.0003:
                    line.append("middle")
                    
                elif 0.0003 <= value:
                    line.append("low")
               
            noise.append(line)
        return noise
            
    def draw(self):
             
        noise = self.color()
        print(noise)
       
       #draw all the chunk
        x,y = 0,0
        from draw_quartier import Quartier
        mark = 0
        for i in noise:
            x = 0
            
            for density in i:
               #draw
               if self.show_perlin == 1:
                    if density == "low":
                        j = "green"
                    elif density == "middle":
                        j= "blue"
                    else:
                        j = "red"
                    self.tu.up()
                    self.tu.goto(self.s_chunk*x, self.s_chunk*y)
                    self.tu.pencolor(j)
                    self.tu.fillcolor(j)
                    self.tu.begin_fill()
                    self.tu.down()
                    for _ in range(2):
                        self.tu.forward(self.s_chunk)
                        self.tu.left(90)
                        self.tu.forward(self.s_chunk) 
                        self.tu.left(90)
                    self.tu.end_fill()
               else:
                    a = Quartier((self.s_chunk*x, self.s_chunk*y), (self.s_chunk*(x+1), self.s_chunk*(y+1)), ra.randint(100000,9999999), density, self.screen, self.c_bg, self.c_house, self.c_road, self.c_line, self.s_chunk, self.s_road, self.s_line)
                    del(a)
                 
               if density == "hight":
                        
                    
                    self.liste_hight.append((x,y))                   
               x += 1
            y += 1

        mark = 0
        print(self.coord)
        self.coord.append([self.liste_hight[0]])
        for i in range(len(self.liste_hight) -1):
            x,y = self.liste_hight[i]
            found,indice = self.coordin(x,y)
            if found:
                self.coord[indice].append((x,y))

            else:
                self.coord.append([(x,y)])
                self.min.append([[1000,1000],[0,0]])
                mark+= 1

            if x < self.min[mark -1][0][0]:
                self.min[mark -1][0][0] = x
            if y < self.min[mark -1][0][1]:
                self.min[mark -1][0][1] = y
            if x > self.min[mark -1][1][0]:
                self.min[mark -1][1][0] = x
            if y > self.min[mark -1][1][1]:
                self.min[mark -1][1][1] = y


        for e in self.coord:
            color = (ra.randint(0,255),ra.randint(0,255),ra.randint(0,255))
            for p in e:
                x,y=p
                
                if self.debug_mode:
                    self.squar(x,y,color,20)

        from noms_villes import ville
        import lib.tkinter as tkinter
        for part in self.min:

            vile = ville()
            x = part[0][0] + round((part[1][0] - part[0][0])* 1/2)
            y = part[0][1] + round((part[1][1] - part[0][1])* 1/2)
            self.tu.up()
            self.tu.goto((x)* self.s_chunk, y * self.s_chunk)
            self.tu.down()
            self.style = ('Courier',self.settings["size_chunk"]//2,'bold')
            self.tu.pencolor(self.c_text)
            self.tu.write(vile,True, align="left", font=self.style)
            self.tu.up()
            self.tu.hideturtle()
            
        
    def squar(self, x, y, color,s):
         
        self.tu.up()
        self.tu.goto(self.s_chunk*x, self.s_chunk*y)
        self.tu.pencolor(color)
        self.tu.fillcolor(color)
        self.tu.begin_fill()
        self.tu.down()
        for _ in range(2):
            self.tu.forward(self.s_chunk-s)
            self.tu.left(90)
            self.tu.forward(self.s_chunk-s) 
            self.tu.left(90)
        self.tu.end_fill()

    def coordin(self, x, y):
        
        for i in range(len(self.coord)):

            for a in range(1,6):
                if (x - a,y + a) in self.coord[i] or (x,y + a) in self.coord[i] or (x + a, y + a) in self.coord[i] or \
                (x - a,y) in self.coord[i] or (x + a, y) in self.coord[i] or (x + a, y+a) in self.coord[i] or \
                (x -a,y - a) in self.coord[i] or (x,y - a) in self.coord[i] or (x + a, y - a) in self.coord[i]:
                
                    #print(x,y, self.coord[i])
                    if self.debug_mode:
                        self.squar(x,y,"orange",5)
                    return True, i
                    
                else:
                    if self.debug_mode:
                        self.squar(x,y,"grey",5)
                    pass
                    #print(x,y, self.coord[i])
        return False,0
            
    def perlin(self):
        #create the perlin noise
        from lib.noise.perlin_noise.perlin_noise import PerlinNoise

        noise1 = PerlinNoise(octaves=self.octaves, seed = self.seed)
        
        y, x = self.width // self.s_chunk + 2, self.height // self.s_chunk + 1
        
        noise = []
        for i in range(x):
            row = []
            for j in range(y):
                noise_val = noise1([i/x, j/y])
                row.append(noise_val)
            
            noise.append(row)
        return noise