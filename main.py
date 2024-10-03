import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("blue")
drawing_board.title("Burak Tablo")



turtle_instance = turtle.Turtle()

def turtle_foward():
    turtle_instance.forward(100)

def rotate_right():
    turtle_instance.right(10)

def rotate_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_screen_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()




drawing_board.listen()
drawing_board.onkey(fun=turtle_foward, key="space")
drawing_board.onkey(fun=rotate_right , key="Down")
drawing_board.onkey(fun=rotate_left , key="Up")
drawing_board.onkey(fun=clear_screen , key="c")
drawing_board.onkey(fun=turtle_screen_home , key="v")

turtle.mainloop()
