import lib.turtle as tu
import lib.random as ra

class Preset:
    def __init__(self, screen, seed, init_x, init_y, x, y, color, pen_color, nb):
        
        #initialise turtle
        self.screen = screen
        self.tu = tu.RawTurtle(self.screen)
        self.tu.setundobuffer(None)
        self.tu.speed(0)
        self.tu.hideturtle()
        self.screen.delay(0)
        ra.seed(seed + nb)
        
        if ra.randint(0,1):
            self.a(init_x, init_y, x, y, color, pen_color)
        else:
            self.b(init_x, init_y, x, y, color, pen_color)
        
    def a(self, init_x, init_y, x, y, color, pen_color):
        orientation = ra.randint(0,2)
        n = ra.randint(20,80)/100
        m = ra.randint(20,80)/100
            
        self.tu.up()
        self.tu.width(1)
        self.tu.pencolor(pen_color)
        self.tu.fillcolor(color)
        self.tu.begin_fill()
        self.tu.seth(0)

        if orientation == 0:
           self.tu.goto(init_x, init_y)
           self.tu.down()
           self.tu.fd(x)
           self.tu.left(90)
           self.tu.fd(y*n)
           self.tu.left(90)
           self.tu.fd(x-x*m)
           self.tu.right(90)
           self.tu.fd(y-y*n)
           self.tu.left(90)
           self.tu.fd(x*m)
           self.tu.left(90)
           self.tu.fd(y)
            
        if orientation == 1:
           self.tu.goto(init_x+(x-x*m), init_y)
           self.tu.down()
           self.tu.fd(x*m)
           self.tu.left(90)
           self.tu.fd(y)
           self.tu.left(90)
           self.tu.fd(x)
           self.tu.left(90)
           self.tu.fd(y*n)
           self.tu.left(90)
           self.tu.fd(x-x*m)
           self.tu.right(90)
           self.tu.fd(y-y*n)
            
        if orientation == 2:
           self.tu.goto(init_x, init_y)
           self.tu.fd(x)
           self.tu.left(90)
           self.tu.fd(y)
           self.tu.left(90)
           self.tu.fd(x*m)
           self.tu.left(90)
           self.tu.fd(y-y*n)
           self.tu.right(90)
           self.tu.fd(x-x*m)
           self.tu.left(90)
           self.tu.fd(y*n)
            
            
        self.tu.end_fill()
        
    def b(self, init_x, init_y, x, y, color,pen_color):
        
        
        self.tu.up()
        self.tu.width(1)
        self.tu.pencolor(pen_color)
        self.tu.fillcolor(color)
        self.tu.begin_fill()
        self.tu.seth(0)
        
        n = ra.randint(50,90)/100
        m = ra.randint(50,90)/100
        
        self.tu.goto(init_x, init_y)
        self.tu.down()
        for _ in range(2):
            self.tu.fd(x*n)
            self.tu.left(90)
            self.tu.fd(y*m)
            self.tu.left(90)
            
        self.tu.end_fill()
        
#         orientation = 0
#         n = ra.randint(10,30)/100
#         m = ra.randint(10,30)/100
#         p = ra.randint(10,30)/100
#         q = ra.randint(10,30)/100
#             
#         self.tu.up()
#         self.tu.width(1)
#         self.tu.pencolor((223,223,221))
#         self.tu.fillcolor(color)
#         self.tu.begin_fill()
#         self.tu.seth(0)
#         
#         if not orientation:
#             self.tu.goto(init_x, init_y)
#             self.tu.fd(x)
#             self.tu.left(90)
#             self.tu.fd(y*n)
#             self.tu.left(90)
#             self.tu.fd(x)
#             self.tu.left(90)
#             self.tu.fd(y*n)
#             self.tu.end_fill()
#             self.tu.up()
#             
#             self.tu.goto(init_x + (x - (x*p))/2, init_y + y*n)
#             self.tu.down()
#             self.tu.begin_fill()
#             self.tu.left(90)
#             self.tu.fd(y*m)
#             self.tu.right(90)
#             self.tu.fd(x*p)
#             self.tu.right(90)
#             self.tu.fd(y*m)
#             self.tu.right(90)
#             self.tu.fd(x*p)
#             self.tu.end_fill()
#             self.tu.up()
#             
#             self.tu.goto(init_x + ((x - (x*p))/2) + ((x -(x*q))/2), init_y + y*n + y*m)
#             self.tu.down()
#             self.tu.begin_fill()
#             self.tu.fd(x*q)
#             self.tu.left(90)
#             self.tu.fd(y-y*n-y*m)
#             self.tu.left(90)
#             self.tu.fd(x*q)
#             self.tu.left(90)
#             self.tu.fd(y-y*n-y*m)
#             self.tu.end_fill()
#             
#       
# for i in range(-2,2):
#     for j in range(-2,2):
#         at.b(i*100,j*100,80,80,"orange")
# tu.mainloop()