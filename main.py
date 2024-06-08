import os
from turtle import *

class FinalSpinner:
    def __init__(self, clr):
        self.clr = clr
        self.state = {'turn': 0}
        self.setup_turtle()
        self.main_spinner()

    def setup_turtle(self):
        """Set up the turtle graphics environment."""
        setup(420, 420, 370, 0)
        color('white')
        hideturtle()
        width(0)
        tracer(False)
        onkeypress(self.flick, 'space')
        listen()

    def spinner(self):
        """Draw the spinner with the current state."""
        clear()
        stick_len = 110
        angle = self.state['turn'] / 10
        
        for _ in range(3):
            right(angle)
            self.draw_stick(stick_len)
            right(120)
            
        dot(110, 'black')
        dot(100, self.clr)
        update()

    def draw_stick(self, length):
        """Draw one stick of the spinner."""
        forward(length)
        dot(130, 'black')
        dot(120, self.clr)
        dot(100, 'gray')
        dot(95, self.clr)
        dot(93, 'black')
        dot(90, 'gray')
        dot(70, 'black')
        dot(60, 'white')
        back(length)

    def animate(self):
        """Animate the spinner by updating its state."""
        if self.state['turn'] > 0:
            self.state['turn'] -= 1
        self.spinner()
        ontimer(self.animate, 20)

    def flick(self):
        """Increase the spinner's turn state."""
        self.state['turn'] += 15

    def main_spinner(self):
        """Initialize and start the spinner animation."""
        self.animate()
        done()

# Create a spinner with a specified color
FinalSpinner('blue') # red, blue, yellow