import argparse
import tkinter as tk
import math

parser = argparse.ArgumentParser(description="A Test for argparse")
parser.add_argument("--theta", action="store")

args = parser.parse_args()
#if args.theta:
#    print(f"Finding theta angle of {args.theta}")

circle_origin_x = 250
circle_origin_y = 250
radius = 100
main_line_length = radius
#used for cos line
main_line_endpoint_x: int = 0
#used for sin line
main_line_endpoint_y: int = 0

def draw_unit_circle() -> None:
    canvas.create_oval(
        circle_origin_x - radius,
        circle_origin_y - radius,
        circle_origin_x + radius,
        circle_origin_y + radius,
        fill="white",
        outline="red",
        width=3,
        )

def draw_x_line() -> None:
    canvas.create_line(
        circle_origin_x - radius,
        circle_origin_y,
        circle_origin_x + radius,
        circle_origin_y,
        fill="black",
        width="1",
    )
def draw_y_line() -> None:
    canvas.create_line(
        circle_origin_x,
        circle_origin_y - radius,
        circle_origin_x,
        circle_origin_y + radius,
        fill="black",
        width="1",
    )

def draw_main_line() -> tuple:
    #convert degrees to radians as math functions use radians
    angle_in_radians = math.radians(int(args.theta))
    #calculate end points with origin at center of unit circle
    #using '-' for y-calculation if you waant 0deg=right, 90deg=up
    x2 = circle_origin_x + main_line_length * math.cos(angle_in_radians)
    y2 = circle_origin_y - main_line_length * math.sin(angle_in_radians)

    #setting global variables
    #global variables need to be changed
    main_line_x = x2
    main_line_y = y2

    #set to return value instead?
    canvas.create_line(
        circle_origin_x,
        circle_origin_y,
        x2,
        y2,
        fill="green",
        width="3",
    )

    return x2, y2

def draw_cosine_line(main_line_x, main_line_y) -> None:
    canvas.create_line(
        circle_origin_x,
        circle_origin_y,
        main_line_x,
        circle_origin_y,
        fill="blue",
        width="3"
    )

def draw_sine_line(main_line_x, main_line_y) -> None:
    canvas.create_line(
        main_line_x,
        main_line_y,
        main_line_x,
        circle_origin_y,
        fill="red",
        width="3",
    )


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, borderwidth=0, highlightthickness=0, bg="black")
canvas.pack(fill="both", expand=True)







draw_unit_circle()
draw_x_line()
draw_y_line()
main_line_endpoint_x, main_line_endpoint_y = draw_main_line()
draw_cosine_line(main_line_endpoint_x, main_line_endpoint_y)
draw_sine_line(main_line_endpoint_x, main_line_endpoint_y)

root.mainloop()