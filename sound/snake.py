import turtle
import time
from random import randint
w=['up','down','left','right']
q=['up','down']
f=['left','right']
def move_ran():
    if ran=='up':
        y=food.ycor()
        food.sety(y+20)
    if ran=='down':
        y=food.ycor()
        food.sety(y-20)
    if ran=='left':
        x=food.xcor()
        food.setx(x+20)
    if ran=='right':
        x=food.xcor()
        food.setx(x-20)
def check_ran():
    if food.xcor()>270 or food.xcor()<-290 or food.ycor()>280 or food.ycor()<-270:
        time.sleep(1)
        food.goto(0,0)


wn = turtle.Screen()
wn.title("snake")
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"


food= turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("black")
food.penup()
food.goto(0,100)

segments = []


sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)



def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


while True:
    wn.update()
    ran=w[randint(0,3)]

    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        
        for segment in segments:
            segment.goto(1000,1000) 
        
        segments.clear()



        sc.clear()
        

    
    if head.distance(food) <20:
        
        x = randint(-290,290)
        y = randint(-290,290)
        food.goto(x,y)

        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        


       

    
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

               
            sc.clear()
    time.sleep(0.1)
    move_ran()
    check_ran()
    time.sleep(0.1)
            
            
wn.mainloop()   