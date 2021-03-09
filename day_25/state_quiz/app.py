import turtle
import pandas


image = 'map.gif'
data = pandas.read_csv('state_data.csv', index_col=0)
# data = data.drop('in', axis=1)
# print(data.to_dict())
# data.state = data.state.apply(lambda name: name.lower())
#
# data.to_csv('state_data.csv')
# print(data[data.index == 'punjab'])


# def take_guess():

def mark_unguessed():
    marker.color('red')
    for s in all_states:
        marker.goto(int(data[data.index == s].x), int(data[data.index == s].y))
        marker.stamp()
        marker.write(s)


screen = turtle.Screen()
screen.addshape(image)
screen.setup(width=640, height=640)
screen.tracer(0)

map_india = turtle.Turtle(shape=image)

marker = turtle.Turtle(visible=False, shape='circle')
marker.shapesize(stretch_len=0.3, stretch_wid=0.3)
marker.up()
all_states = data.index.to_list()

lives = 3
life = turtle.Turtle(shape='square')
life.up()
life.color('red')
life.shapesize(stretch_len=lives, stretch_wid=0.5)
life.goto(260, 300)
life.write('Life', font=('Arial', 14, 'bold'), align='center')
life.goto(260, 295)

while True:
    screen.update()
    if lives <= 0:

        mark_unguessed()
        break
    state = screen.textinput(title=f'Left: {len(all_states)}/29', prompt='Enter the Full name of state.').lower()
    if state not in all_states:
        lives -= 1
        life.shapesize(stretch_len=lives if lives != 0 else 0.001, stretch_wid=0.5)
        print(lives)
        continue
    x, y = int(data[data.index == state].x), int(data[data.index == state].y)
    all_states.remove(state)
    marker.goto(x, y)
    marker.color('green')
    marker.stamp()
    marker.color('green')
    marker.write(state.title())
    print(x, y)
    if len(all_states) == 0:
        marker.home()
        marker.pencolor('green')
        marker.write('YOU WON', font=('Arial', 40, 'bold'), align='center')
        break

print(all_states)
screen.exitonclick()
