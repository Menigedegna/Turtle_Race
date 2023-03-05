from turtle import Turtle, Screen
from random import randint


class TURTLE:

    def __init__(self, color):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.fillcolor(color)

    def move_forward(self):
        random_distance = randint(0, 10)
        self.turtle.forward(random_distance)


class Race:

    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.title("Turtle Race")
        self.width = 500
        self.height = 400
        self.screen.setup(width=self.width, height=self.height, startx=0, starty=0)
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.user_bet = ""
        self.max_distance = round(self.width/2) - 30

    def prompt_user_choice(self):
        # ask user to bet on turtle
        while self.user_bet == "" or self.user_bet not in self.colors:
            self.user_bet = self.screen.textinput("Make your bet", "Who will win the race? Enter a colour: ")

    def place_finish_line(self):
        finish_line = Turtle()
        finish_line.penup()
        x_position = (self.max_distance, round(self.height/2)-20)
        finish_line.goto(x_position)
        finish_line.right(90)
        finish_line.pendown()
        finish_line.pensize(10)
        finish_line.pencolor("white")
        finish_line.forward(self.height-20)
        finish_line.hideturtle()

    def place_turtles(self):
        """return list of TURTLE instances"""
        x_offset = int((-1*self.width/2) + 20)
        y_offset = int((-1*self.height/2) + 20)
        home = (x_offset, y_offset)
        y_offset = 50
        turtle_list = []
        for col in self.colors:
            my_racer = TURTLE(col)
            home = (home[0], home[1] + y_offset)
            my_racer.turtle.speed(10)
            my_racer.turtle.penup()
            my_racer.turtle.goto(home)
            turtle_list.append(my_racer)
        return turtle_list

    def get_winner(self, list_turtles, furthest_turtle):
        """prints whether user won or lost"""
        distance_list = [my_racer.turtle.position()[0] for my_racer in list_turtles]
        winner_turtle = distance_list.index(furthest_turtle)
        # check if user won and inform user
        user_turtle = self.colors.index(self.user_bet)
        if user_turtle == winner_turtle:
            print("You've won!")
        else:
            print(f"You've lost! The {self.colors[winner_turtle]} turtle is the winner.")

    def clean(self):
        print("cleaning")
        self.screen.reset()
        self.user_bet = ""

    def start_race(self):
        if self.user_bet != "":
            self.clean()
        # ask user to bet on turtle
        self.prompt_user_choice()
        # draw finish line
        self.place_finish_line()
        # place turtles
        list_turtles = self.place_turtles()
        # start race
        furthest_turtle = 0
        while furthest_turtle < self.max_distance:
            for my_racer in list_turtles:
                my_racer.move_forward()
                furthest_turtle = max(furthest_turtle, my_racer.turtle.position()[0])
        # deduce winner
        self.get_winner(list_turtles, furthest_turtle)
        self.screen.listen()
        self.screen.onkey(key="space", fun=self.start_race)


