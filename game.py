import turtle
import random

drawing_board= turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Kaplumbağa Yakalamaca")

turtle_instance= turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.penup()

score_writer= turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0,270)
score= 0

countdown_writer= turtle.Turtle()
countdown_writer.hideturtle()
countdown_writer.penup()
countdown_writer.goto(0,230)
time= 30
timer_id= None

def turtle_click(x,y):
    global score
    print("Yakalandın!")
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    move_turtle()

def move_turtle():
    global timer_id
    if timer_id:
        drawing_board.getcanvas().after_cancel(timer_id)

    if turtle_instance.isvisible():
        turtle_instance.hideturtle()
        turtle_instance.goto(random.randint(-250,250), random.randint(-250,250))
        turtle_instance.showturtle()
        
        timer_id= drawing_board.getcanvas().after(1000, move_turtle)

def start_timer(time):
    countdown_writer.clear()
    if time > 0:
        countdown_writer.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))
        drawing_board.ontimer(lambda: start_timer(time - 1), 1000)
    else:
        countdown_writer.write("OYUN BİTTİ!", align="center", font=("Arial", 24, "normal"))
        turtle_instance.hideturtle()
        turtle_instance.onclick(None)

drawing_board.listen()
turtle_instance.onclick(turtle_click)

turtle_instance.speed(0)
start_timer(30)
move_turtle()
turtle.done()