import turtle

# Draw a Square
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

# Draw a Circle Using Squares
def draw_circle_with_squares():
    # Open a Window
    window = turtle.Screen()
    # In Red Color
    window.bgcolor("red")

    # Create the Bruno Turtle and Draws a Square
    bruno = turtle.Turtle()
    bruno.shape("turtle")
    bruno.color("yellow")
    bruno.speed(10)
    for i in range(1,73):
        draw_square(bruno)
        bruno.right(5)

    # Close the Window on Click
    window.exitonclick()

# Draw a Lozenge
def draw_lozenge(some_turtle):
    for i in range(1,3):
        some_turtle.forward(70)
        some_turtle.right(53.13)
        some_turtle.forward(70)
        some_turtle.right(126.87)


# Draw a Flower With Lozenges
def draw_flower_with_lozenge():
    # Open a Window
    window = turtle.Screen()
    # In Red Color
    window.bgcolor("red")

    # Create the Bruno Turtle and Draws a Square
    bruno = turtle.Turtle()
    bruno.shape("turtle")
    bruno.color("blue")
    bruno.speed(100)
    for i in range(1,37):
        draw_lozenge(bruno)
        bruno.right(10)
    
    bruno.right(90)
    bruno.forward(180)

    # Close the Window on Click
    window.exitonclick()

#draw_flower_with_lozenge()

#draw_circle_with_squares()