import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Collect the Coins!")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Set up the turtle for the player
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# Set up the turtle for the coins
coins = []
for i in range(10):
    coin = turtle.Turtle()
    coin.shape("circle")
    coin.color("yellow")
    coin.penup()
    coin.goto(random.randint(-280, 280), random.randint(-280, 280))
    coins.append(coin)

# Define a function to move the player
def move_player_left():
    player.setheading(180)
    player.forward(10)

def move_player_right():
    player.setheading(0)
    player.forward(10)

def move_player_up():
    player.setheading(90)
    player.forward(10)

def move_player_down():
    player.setheading(270)
    player.forward(10)

# Set up the key bindings
screen.onkey(move_player_left, "Left")
screen.onkey(move_player_right, "Right")
screen.onkey(move_player_up, "Up")
screen.onkey(move_player_down, "Down")
screen.listen()

# Define a function to check if the player has collided with a coin
def check_collision(coin, player):
    x_diff = coin.xcor() - player.xcor()
    y_diff = coin.ycor() - player.ycor()
    distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
    if distance < 20:
        return True
    else:
        return False

# Set up the game loop
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-280, 260)
score_turtle.write("Score: {}".format(score), font=("Arial", 16, "normal"))
while True:
    for coin in coins:
        if check_collision(coin, player):
            coin.hideturtle()
            coins.remove(coin)
            score += 1
            score_turtle.clear()
            score_turtle.write("Score: {}".format(score), font=("Arial", 16, "normal"))
    if not coins:
        score_turtle.goto(0, 0)
        score_turtle.write("You won!", align="center", font=("Arial", 24, "normal"))
        break
