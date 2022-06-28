import random
from turtle import Turtle

color=["green","orange","red","blue","purple","violet","black","pink"]
class CarManager:
    def __init__(self):
        self.all_cars=[]
    def create_car(self):
        random_number=random.randint(1,6)
        if(random_number==1):
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(color))
            new_y=random.randint(-250,250)
            new_car.goto(450,new_y)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(5)
