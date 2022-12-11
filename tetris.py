'''
Options Implemented: Option 2: Different Tetraminoes
                     Option 6: Game Over
'''

import turtle, random

SCALE = 32 #Controls how many pixels wide each grid square is

class Game:
    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)
        self.occupied = []

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        
        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)

        self.active = Block()
        turtle.ontimer(self.gameloop, 300)
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if self.active.valid(0, -1, self.occupied):
            self.active.move(0, -1)
        else:
            for square in self.active.squares:
                self.occupied.append([square.xcor(), square.ycor()])
                if square.ycor() == 20:
                    print("Game Over")
                    turtle.write("GAME OVER!", font = ("Verdana", 40, "normal"))
                    return None
            self.active = Block()
        turtle.update()
        turtle.ontimer(self.gameloop, 50)

    def move_left(self):
        if self.active.valid(-1, 0, self.occupied):
            self.active.move(-1, 0)
        turtle.update()

    def move_right(self):
        if self.active.valid(1, 0, self.occupied):
            self.active.move(1, 0)
        turtle.update()



class Square(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)

        self.shape("square")
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor("gray")
        self.penup()
        self.goto(x, y)

class Block:
    def __init__(self):
        self.squares = []
        tetr = random.randint(1, 7)
        match tetr:
            case 1:
                self.I_shape()
            case 2:
                self.L_shape()
            case 3:
                self.J_shape()
            case 4:
                self.O_shape()
            case 5:
                self.S_shape()
            case 6:
                self.T_shape()
            case 7:
                self.Z_shape()

    def I_shape(self):
        sq1 = Square(3, 21, "cyan")
        sq2 = Square(4, 21 , "cyan")
        sq3 = Square(5, 21 , "cyan")
        sq4 = Square(6, 21 , "cyan")
        self.squares += [sq1, sq2, sq3, sq4]
    
    def L_shape(self):
        sq1 = Square(4, 22, "blue")
        sq2 = Square(4, 21 , "blue")
        sq3 = Square(5, 21 , "blue")
        sq4 = Square(6, 21 , "blue")
        self.squares += [sq1, sq2, sq3, sq4]

    def J_shape(self):
        sq1 = Square(6, 22, "orange")
        sq2 = Square(4, 21 , "orange")
        sq3 = Square(5, 21 , "orange")
        sq4 = Square(6, 21 , "orange")
        self.squares += [sq1, sq2, sq3, sq4]

    def O_shape(self):
        sq1 = Square(4, 22, "yellow")
        sq2 = Square(4, 21 , "yellow")
        sq3 = Square(5, 21 , "yellow")
        sq4 = Square(5, 22 , "yellow")
        self.squares += [sq1, sq2, sq3, sq4]

    def S_shape(self):
        sq1 = Square(4, 21, "green")
        sq2 = Square(5, 21 , "green")
        sq3 = Square(5, 22 , "green")
        sq4 = Square(6, 22 , "green")
        self.squares += [sq1, sq2, sq3, sq4]

    def T_shape(self):
        sq1 = Square(5, 22, "purple")
        sq2 = Square(4, 21 , "purple")
        sq3 = Square(5, 21 , "purple")
        sq4 = Square(6, 21 , "purple")
        self.squares += [sq1, sq2, sq3, sq4]

    def Z_shape(self):
        sq1 = Square(4, 22, "red")
        sq2 = Square(5, 22 , "red")
        sq3 = Square(5, 21 , "red")
        sq4 = Square(6, 21 , "red")
        self.squares += [sq1, sq2, sq3, sq4]

    def move(self, dx, dy):
        for sq_obj in self.squares:
            x_cor = sq_obj.xcor()
            y_cor = sq_obj.ycor()
            x_cor += dx
            y_cor += dy
            sq_obj.goto(x_cor, y_cor)

    def valid(self, dx, dy, occupied):
        ret_val = True
        for sq_obj in self.squares:
            x_cor = sq_obj.xcor()
            y_cor = sq_obj.ycor()
            x_cor += dx
            y_cor += dy
            if x_cor < 0 or x_cor > 9 or y_cor < 0:
                ret_val = False
            if [x_cor, y_cor] in occupied:
                ret_val = False
        return ret_val



if __name__ == '__main__':
    Game()
