import turtle
import time
import random

delay = 0.1
score = 0
High_score = 0

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.cv._rootwindow.resizable(False, False)
window.tracer(0)

head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.speed(0)
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(["red", "green", "black"])
shapes = random.choice(["square", "circle"])
food.shape(shapes)
food.color(colors)
food.penup()
food.speed(0)
food.goto(0, 100)

pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0, 250)
pen.hideturtle()
pen.write("Score: 0    High Score: 0", align="center", font=("Arial", 24, "bold"))


def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


window.listen()
window.onkeypress(goup, "w")
window.onkeypress(godown, "s")
window.onkeypress(goleft, "a")
window.onkeypress(goright, "d")

segments = []

while True:
    window.update()

    
    if (
            head.xcor() > 290
            or head.xcor() < -290
            or head.ycor() > 290
            or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(["red", "green", "black"])
        shapes = random.choice(["circle", "square"])
        food.color(colors)
        food.shape(shapes)
        for segment in segments:
            segment.hideturtle()
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(
            "Score: {}    High Score: {}".format(score, High_score),
            align="center",
            font=("Arial", 24, "bold"),
        )


    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > High_score:
            High_score = score
        pen.clear()
        pen.write(
            "Score: {}    High Score: {}".format(score, High_score),
            align="center",
            font=("Arial", 24, "bold"),
        )

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()


    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(["red", "green", "black"])
            shapes = random.choice(["square", "circle"])
            food.color(colors)
            food.shape(shapes)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(
                "Score: {}    High Score: {}".format(score, High_score),
                align="center",
                font=("Arial", 24, "bold"),
            )

    time.sleep(delay)