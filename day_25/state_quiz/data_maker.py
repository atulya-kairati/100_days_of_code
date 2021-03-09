import turtle
import pandas

state_coords = {
    'state': [],
    'x': [],
    'y': []
}
image = 'map.gif'
screen = turtle.Screen()
screen.addshape(image)
screen.setup(height=640, width=640)

t = turtle.Turtle(shape=image)
marker = turtle.Turtle(shape='circle', visible=False)
marker.shapesize(stretch_len=0.2, stretch_wid=0.2)
marker.up()


def click_fun(x, y):
    state = screen.textinput(title='INPUT', prompt='Enter the State Name on "e" to end')
    if state == 'e' or state == '':
        data = pandas.DataFrame(state_coords)
        data.to_csv('state_data.csv')
        screen.bye()
    state_coords['state'].append(state)
    state_coords['x'].append(x)
    state_coords['y'].append(y)
    marker.goto(x, y)
    marker.stamp()
    print(state_coords)


def save_exit():
    data = pandas.DataFrame(state_coords)
    data.to_csv('state_data.csv')
    screen.bye()


screen.listen()
screen.onkeypress(fun=save_exit, key='S')

screen.onclick(fun=click_fun)
turtle.mainloop()
