import turtle as t
import time

# Global variables
playerAscore = 0
playerBscore = 0
running = False
in_menu = True

# Setup main screen
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Function to initialize game objects
def setup_game():
    global leftpaddle, rightpaddle, ball, pen, ballxdirection, ballydirection
    
    # Creating the left paddle
    leftpaddle = t.Turtle()
    leftpaddle.speed(0)
    leftpaddle.shape("square")
    leftpaddle.color("white")
    leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
    leftpaddle.penup()
    leftpaddle.goto(-350, 0)
    
    # Creating the right paddle
    rightpaddle = t.Turtle()
    rightpaddle.speed(0)
    rightpaddle.shape("square")
    rightpaddle.color("white")
    rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
    rightpaddle.penup()
    rightpaddle.goto(350, 0)
    
    # Code for creating the ball
    ball = t.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(5, 5)
    ballxdirection = 10  # Ball Speed X
    ballydirection = 10   # Ball speed Y
    
    # Code for creating pen for scorecard update
    pen = t.Turtle()
    pen.speed(0)
    pen.color("Blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0                    Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Code for moving the leftpaddle
def leftpaddleup():
    if running:
        y = leftpaddle.ycor()
        y = y + 90
        leftpaddle.sety(y)

def leftpaddledown():
    if running:
        y = leftpaddle.ycor()
        y = y - 90
        leftpaddle.sety(y)

# Code for moving the rightpaddle
def rightpaddleup():
    if running:
        y = rightpaddle.ycor()
        y = y + 90
        rightpaddle.sety(y)

def rightpaddledown():
    if running:
        y = rightpaddle.ycor()
        y = y - 90
        rightpaddle.sety(y)

# Function to exit game
def exit_game():
    global running
    running = False
    window.bye()

# Function to create and display the main menu
def show_main_menu():
    global menu_title, start_button, exit_button, in_menu
    
    # Clear any existing game elements
    window.clear()
    window.bgcolor("black")
    
    # Create menu title
    menu_title = t.Turtle()
    menu_title.speed(0)
    menu_title.color("white")
    menu_title.penup()
    menu_title.hideturtle()
    menu_title.goto(0, 100)
    menu_title.write("PONG GAME", align="center", font=('Arial', 36, 'bold'))
    
    # Create start button
    start_button = t.Turtle()
    start_button.speed(0)
    start_button.shape("square")
    start_button.color("green")
    start_button.shapesize(stretch_wid=2, stretch_len=10)
    start_button.penup()
    start_button.goto(0, 0)
    
    # Create button text
    start_text = t.Turtle()
    start_text.speed(0)
    start_text.color("white")
    start_text.penup()
    start_text.hideturtle()
    start_text.goto(0, -5)
    start_text.write("START GAME", align="center", font=('Arial', 14, 'bold'))
    
    # Create exit button
    exit_button = t.Turtle()
    exit_button.speed(0)
    exit_button.shape("square")
    exit_button.color("red")
    exit_button.shapesize(stretch_wid=2, stretch_len=10)
    exit_button.penup()
    exit_button.goto(0, -80)
    
    # Create exit button text
    exit_text = t.Turtle()
    exit_text.speed(0)
    exit_text.color("white")
    exit_text.penup()
    exit_text.hideturtle()
    exit_text.goto(0, -85)
    exit_text.write("EXIT", align="center", font=('Arial', 14, 'bold'))
    
    # Add controls info
    controls = t.Turtle()
    controls.speed(0)
    controls.color("yellow")
    controls.penup()
    controls.hideturtle()
    controls.goto(0, -150)
    controls.write("CONTROLS: W/S - Left paddle, UP/DOWN - Right paddle, ESC - Quit", 
                  align="center", font=('Arial', 12, 'normal'))
    
    # Click handlers for buttons
    window.listen()
    window.onkeypress(start_game, "Return")  # Enter key also starts the game
    window.onclick(handle_click)
    
    in_menu = True
    
    # Menu update loop
    while in_menu:
        window.update()
        time.sleep(0.01)

# Function to handle mouse clicks
def handle_click(x, y):
    global in_menu
    
    # Check if click is on start button
    if in_menu and x > -100 and x < 100 and y > -20 and y < 20:
        in_menu = False
        start_game()
    
    # Check if click is on exit button
    if in_menu and x > -100 and x < 100 and y > -100 and y < -60:
        exit_game()

# Function to start the game
def start_game():
    global running, in_menu, playerAscore, playerBscore
    
    # Reset scores
    playerAscore = 0
    playerBscore = 0
    
    # Clear menu items
    window.clear()
    window.bgcolor("green")
    
    # Setup game elements
    setup_game()
    
    # Setup key bindings
    window.listen()
    window.onkeypress(leftpaddleup, 'w')
    window.onkeypress(leftpaddledown, 's')
    window.onkeypress(rightpaddleup, 'Up')
    window.onkeypress(rightpaddledown, 'Down')
    window.onkeypress(exit_game, "Escape")  # ESC key to exit
    
    in_menu = False
    running = True
    run_game()

# Main game loop
def run_game():
    global playerAscore, playerBscore, running, ballxdirection, ballydirection
    
    while running:
        try:
            window.update()
            
            # Moving the ball
            ball.setx(ball.xcor() + ballxdirection)
            ball.sety(ball.ycor() + ballydirection)
            
            # Border set up
            if ball.ycor() > 290:
                ball.sety(290)
                ballydirection = ballydirection * -1
            if ball.ycor() < -290:
                ball.sety(-290)
                ballydirection = ballydirection * -1
                
            if ball.xcor() > 390:
                ball.goto(0, 0)
                ballxdirection = ballxdirection * -1
                playerAscore = playerAscore + 1
                pen.clear()
                pen.write("Player A: {}                    Player B: {} ".format(playerAscore, playerBscore), 
                          align="center", font=('Arial', 24, "normal"))
            
            if ball.xcor() < -390:  # Left width paddle Border
                ball.goto(0, 0)
                ballxdirection = ballxdirection * -1
                playerBscore = playerBscore + 1
                pen.clear()
                pen.write("Player A: {}                    Player B: {} ".format(playerAscore, playerBscore), 
                          align="center", font=('Arial', 24, "normal"))
            
            # Handling the collisions with paddles.
            if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
                ball.setx(340)
                ballxdirection = ballxdirection * -1
            
            if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
                ball.setx(-340)
                ballxdirection = ballxdirection * -1
                
            time.sleep(0.01)  # Add a small delay to control game speed
                
        except t.Terminator:
            running = False  # Exit the loop if window is closed
        except Exception as e:
            print(f"An error occurred: {e}")
            running = False  # Exit on any other error
    
    # After game ends, show menu again
    if not window._RUNNING:
        return
    show_main_menu()

# Start with main menu
show_main_menu()

# Handle window close event properly
window.mainloop()