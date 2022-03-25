"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, randint, choice
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Se crean los vectores de comida, longitud, direccion y colores
food = vector(0, 0)     
snake = [vector(10, 0)]     
aim = vector(0, -10)    
colores = ['orange', 'blue', 'black', 'purple', 'green', 'pink']

# Se elige un color al azar para la comida y la serpiente
colorFood = choice(colores)  
colores.remove(colorFood)   
colorSnake = choice(colores)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def moveFood():
    global food
    if(inside(food)):
        aimFood = vector(randint(-1, 1) * 10, randint(-1, 1) * 10)
        food.move(aimFood)  # Mueve la comida
    else:
        food = vector(0, 0)
    ontimer(moveFood, 1000) # Se repite cada 1000ms
    
    
def move():
    """Move snake forward one segment anf food one step at a time."""
    head = snake[-1].copy()
    head.move(aim)
    #Move food randomly 1 step at a time
    food.move(randrange(-5, 5))

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
