import os
from turtle import *
class final_spinner:
  def __init__(self, clr):
    self.clr = clr
    state = {'turn': 0}
    def main_spinner():
        def spinner():
            clear()
            dot(130, 'black')
            dot(120, self.clr)
            angle = state['turn'] / 10
            right(angle)
            stick_len = 110
            forward(stick_len)
            dot(130, 'black')
            dot(120, self.clr)
            dot(100, 'gray')
            dot(95, self.clr)
            dot(93, 'black')
            dot(90, 'gray')
            dot(70, 'black')
            dot(60, 'white')
            back(stick_len)
            right(120)
            val = 170
            forward(stick_len)
            dot(130, 'black')
            dot(120, clr)
            dot(100, 'gray')
            dot(95, clr)
            dot(93, 'black')
            dot(90, 'gray')
            dot(70, 'black')
            dot(60, 'white')
            back(stick_len)
            right(120)
            val = 30
            forward(stick_len)
            dot(130, 'black')
            dot(120, clr)
            dot(100, 'gray')
            dot(95, clr)
            dot(93, 'black')
            dot(90, 'gray')
            dot(70, 'black')
            dot(60, 'white')
            back(stick_len)
            right(120)
            dot(110, 'black')
            dot(100, clr)
            update()

        def animate():
            if state['turn'] > 0:
                state['turn'] -= 1
            spinner()
            ontimer(animate, 20)

        def flick():
            state['turn'] += 15

        setup(420, 420, 370, 0)
        color('white')
        hideturtle()
        width(0)
        tracer(False)
        onkeypress(flick, 'space')
        listen()
        animate()
        done()
    main_spinner()
mydir = "/Users/sai/Desktop/everything/Programming/Major projects/Fidget spinner/color"
for root, dirs, files in os.walk(mydir):
    for filename in files:
        clr = (filename)
# mention the file path in the 73rd line and put clr in place of 'red' . You can simply put 'blue','yellow' etc inplace of 'red in below line
p1 = final_spinner('red')
