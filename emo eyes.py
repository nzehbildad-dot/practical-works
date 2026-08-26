import turtle
import random
import math

# ============================================================
# AUTONOMOUS DESK BOT
# No keyboard commands.
#
# The face behaves on its own:
#   - blinks naturally
#   - looks around
#   - looks at the mouse when it moves
#   - becomes curious / happy / sleepy / surprised
#   - makes tiny eye movements
#   - occasionally smiles
#
# Just run the file and leave it alone.
# ============================================================

screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("#111318")
screen.title("Autonomous Desk Bot")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


# -----------------------------
# State
# -----------------------------

FACE_X = 0
FACE_Y = 10
FACE_W = 330
FACE_H = 270

mouse_x = 0
mouse_y = 0
mouse_moving = False

# Current eye target relative to the face
look_x = 0
look_y = 0

# Target the eyes gradually move toward
target_look_x = 0
target_look_y = 0

expression = "happy"

# Blink state
blink = False
blink_progress = 0.0

# Animation counters
frame = 0
next_blink = random.randint(90, 220)
next_look = random.randint(60, 150)
next_expression = random.randint(300, 700)

# Mouse activity
mouse_idle_frames = 0


# -----------------------------
# Drawing
# -----------------------------

def rounded_face():
    """Draw a rounded robot-like face."""
    pen.penup()
    pen.goto(-FACE_W / 2, -FACE_H / 2 + FACE_Y)
    pen.setheading(0)
    pen.pendown()

    pen.fillcolor("#D7D7D7")
    pen.pencolor("#D7D7D7")
    pen.begin_fill()

    # Rounded rectangle
    r = 45
    straight_w = FACE_W - 2 * r
    straight_h = FACE_H - 2 * r

    pen.forward(straight_w)
    pen.circle(r, 90)
    pen.forward(straight_h)
    pen.circle(r, 90)
    pen.forward(straight_w)
    pen.circle(r, 90)
    pen.forward(straight_h)
    pen.circle(r, 90)

    pen.end_fill()


def draw_eye(x, y, pupil_x, pupil_y, openness=1.0):
    """Draw one eye and its moving pupil."""
    eye_w = 70
    eye_h = 75 * openness

    if eye_h < 4:
        # Closed eye
        pen.penup()
        pen.goto(x - 28, y)
        pen.pendown()
        pen.pencolor("#050505")
        pen.pensize(10)
        pen.goto(x + 28, y)
        pen.penup()
        return

    # Eye white
    pen.penup()
    pen.goto(x, y - eye_h / 2)
    pen.setheading(0)
    pen.pendown()

    pen.fillcolor("#F4F4F4")
    pen.pencolor("#F4F4F4")
    pen.begin_fill()

    # Ellipse
    for _ in range(2):
        pen.circle(eye_w / 2, 90)
        pen.circle(eye_h / 2, 90)

    pen.end_fill()

    # Pupil
    px = x + pupil_x
    py = y + pupil_y

    pupil_size = 19

    pen.penup()
    pen.goto(px, py - pupil_size)
    pen.pendown()
    pen.fillcolor("#050505")
    pen.pencolor("#050505")
    pen.begin_fill()
    pen.circle(pupil_size)
    pen.end_fill()

    # Tiny reflection
    pen.penup()
    pen.goto(px - 6, py + 7)
    pen.pendown()
    pen.fillcolor("#FFFFFF")
    pen.pencolor("#FFFFFF")
    pen.begin_fill()
    pen.circle(4)
    pen.end_fill()


def draw_mouth():
    """Draw a mouth based on the current expression."""
    pen.pencolor("#050505")
    pen.pensize(10)

    if expression == "happy":
        # Smile
        pen.penup()
        pen.goto(-75, -70)
        pen.setheading(-35)
        pen.pendown()
        pen.circle(90, 70)
        pen.penup()

    elif expression == "sad":
        # Frown
        pen.penup()
        pen.goto(-75, -45)
        pen.setheading(35)
        pen.pendown()
        pen.circle(-90, 70)
        pen.penup()

    elif expression == "surprised":
        # Open mouth
        pen.penup()
        pen.goto(0, -90)
        pen.pendown()
        pen.fillcolor("#050505")
        pen.pencolor("#050505")
        pen.begin_fill()
        pen.circle(24)
        pen.end_fill()

    elif expression == "sleepy":
        # Small relaxed mouth
        pen.penup()
        pen.goto(-35, -75)
        pen.pendown()
        pen.goto(35, -75)
        pen.penup()

    elif expression == "curious":
        # Slight smile
        pen.penup()
        pen.goto(-45, -75)
        pen.setheading(-25)
        pen.pendown()
        pen.circle(55, 50)
        pen.penup()

    else:
        # Neutral
        pen.penup()
        pen.goto(-45, -75)
        pen.pendown()
        pen.goto(45, -75)
        pen.penup()


def draw_eyebrows():
    if expression == "curious":
        pen.pencolor("#050505")
        pen.pensize(7)

        pen.penup()
        pen.goto(-105, 75)
        pen.pendown()
        pen.goto(-45, 85)

        pen.penup()
        pen.goto(45, 85)
        pen.pendown()
        pen.goto(105, 75)
        pen.penup()

    elif expression == "sad":
        pen.pencolor("#050505")
        pen.pensize(7)

        pen.penup()
        pen.goto(-105, 85)
        pen.pendown()
        pen.goto(-45, 75)

        pen.penup()
        pen.goto(45, 75)
        pen.pendown()
        pen.goto(105, 85)
        pen.penup()


def draw_face():
    pen.clear()

    rounded_face()

    # Blink animation
    if blink:
        openness = max(0.02, 1.0 - blink_progress)
    else:
        openness = 1.0

    # Make sleepy eyes naturally half closed
    if expression == "sleepy" and not blink:
        openness = 0.45

    # X eyes are used only briefly for the classic happy look.
    # Most of the time the pupils move naturally.
    draw_eye(-75, 55, look_x, look_y, openness)
    draw_eye(75, 55, look_x, look_y, openness)

    draw_eyebrows()
    draw_mouth()

    screen.update()


# -----------------------------
# Mouse tracking
# -----------------------------

def mouse_move(event):
    global mouse_x, mouse_y, mouse_moving, mouse_idle_frames

    mouse_x = event.x - screen.window_width() / 2
    mouse_y = screen.window_height() / 2 - event.y

    mouse_moving = True
    mouse_idle_frames = 0


screen.getcanvas().bind("<Motion>", mouse_move)


# -----------------------------
# Choose where to look
# -----------------------------

def choose_look_target():
    global target_look_x, target_look_y

    # Sometimes look toward the mouse if it is active.
    if mouse_moving and random.random() < 0.65:
        dx = mouse_x
        dy = mouse_y - 30

        distance = math.hypot(dx, dy)

        if distance > 0:
            amount = min(24, distance / 8)
            target_look_x = (dx / distance) * amount
            target_look_y = (dy / distance) * amount
        return

    # Otherwise look around like a person thinking.
    directions = [
        (-22, 0),      # left
        (22, 0),       # right
        (0, 15),       # up
        (0, -10),      # down
        (-14, 8),
        (14, 8),
        (0, 0),        # center
        (0, 0),
        (0, 0),
    ]

    target_look_x, target_look_y = random.choice(directions)


# -----------------------------
# Natural blinking
# -----------------------------

def start_blink():
    global blink, blink_progress

    if not blink:
        blink = True
        blink_progress = 0.0


def update_blink():
    global blink, blink_progress, next_blink

    if blink:
        # Close quickly, then open quickly.
        blink_progress += 0.16

        if blink_progress >= 1.0:
            blink = False
            blink_progress = 0.0

            # Human-ish random interval until next blink.
            next_blink = random.randint(100, 280)


# -----------------------------
# Natural expressions
# -----------------------------

def choose_expression():
    global expression, next_expression

    # Keep happy/neutral more common.
    choices = [
        "happy",
        "happy",
        "happy",
        "neutral",
        "neutral",
        "curious",
        "sleepy",
        "surprised",
        "sad",
    ]

    expression = random.choice(choices)
    next_expression = random.randint(350, 850)


# -----------------------------
# Main autonomous animation
# -----------------------------

def animate():
    global frame
    global look_x, look_y
    global target_look_x, target_look_y
    global next_blink, next_look, next_expression
    global mouse_moving, mouse_idle_frames

    frame += 1
    mouse_idle_frames += 1

    # Mouse only counts as active for a short period.
    if mouse_idle_frames > 120:
        mouse_moving = False

    # Blink
    if not blink:
        next_blink -= 1

        if next_blink <= 0:
            start_blink()

    update_blink()

    # Pick a new place to look
    next_look -= 1

    if next_look <= 0:
        choose_look_target()
        next_look = random.randint(50, 170)

    # Smoothly move eyes instead of teleporting them.
    look_x += (target_look_x - look_x) * 0.10
    look_y += (target_look_y - look_y) * 0.10

    # Occasionally change mood
    next_expression -= 1

    if next_expression <= 0:
        choose_expression()

    draw_face()

    # About 50 frames per second.
    screen.ontimer(animate, 20)


# Start
choose_look_target()
draw_face()
animate()

screen.mainloop()