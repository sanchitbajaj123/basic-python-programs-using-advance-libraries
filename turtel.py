import tkinter
import turtle
import tkinter.messagebox

window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw = turtle.Turtle()
draw = turtle.RawTurtle(canvas)

def Board(a, x, y, size):
    #draw.pu()
    draw.penup()
    draw.goto(x,y)
    #draw.pd()
    draw.pendown()
    for i in range (0, 4):
        draw.forward(size)
        draw.right(90)

def Board2():
    x =-40
    y = -40
    size = 40
    for i in range (0, 10):
        for j in range (0, 10):
            Board(draw, x + j*size, y + i*size, size)

def Button_click ():
    tkinter.messagebox.showinfo("Game", "Tic Tac Toe")

#button = tkinter.Button(window, text = "Play!", command = Button_click)
#button = Tk.Button(window, text = "Play!", command = Button_click)
#button.pack()
#
Play_Button = tkinter.Button(master = window, text ="Play!", command = Button_click)
Play_Button.config(bg="cyan",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Draw_Board", command = Board2)
Board_Button.config(bg="cyan",fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')
#
window.mainloop()
