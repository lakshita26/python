from turtle import Turtle, Screen
import time
from random import randint, choice

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


player = Player()

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS = ["red", "orange", "blue", "green", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-200, 200)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


cars = CarManager()

FONT = ("Courier", 18, "normal")
FONT_GAME_OVER = ("Bold", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-240, 260)
        self.level = 1
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", align=ALIGNMENT, font=FONT_GAME_OVER)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()


levels = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # Detect the collision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            levels.game_over()

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        levels.increase_level()

screen.exitonclick()
