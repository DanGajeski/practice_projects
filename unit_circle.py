import argparse
import math
import tkinter as tk

import unit_circle_class as ucc

parser = argparse.ArgumentParser(description="A Test for argparse")
parser.add_argument("--theta", action="store")

args = parser.parse_args()
# if args.theta:
#    print(f"Finding theta angle of {args.theta}")

# circle_origin_x = 250
# circle_origin_y = 250
# radius = 100
# main_line_length = radius
# # used for cos line
# main_line_endpoint_x: int = 0
# # used for sin line
# main_line_endpoint_y: int = 0


# def draw_title() -> None:  # draws title text centered
#     canvas.create_text(
#         circle_origin_x,
#         50,
#         text="The Unit Circle\nPlotting Sine and Cosine",
#         font=("Arial", 25, "bold"),
#         justify="center",
#         fill="black",
#         anchor="center",
#     )


# def draw_unit_circle() -> None:  # draws main unit circle
#     canvas.create_oval(
#         circle_origin_x - radius,
#         circle_origin_y - radius,
#         circle_origin_x + radius,
#         circle_origin_y + radius,
#         fill="white",
#         outline="black",
#         width=2,
#     )


# def draw_x_line() -> None:  # draws unit circle x line
#     canvas.create_line(
#         circle_origin_x - radius,
#         circle_origin_y,
#         circle_origin_x + radius,
#         circle_origin_y,
#         fill="black",
#         width="1",
#     )


# def draw_y_line() -> None:  # draws unit circle y line
#     canvas.create_line(
#         circle_origin_x,
#         circle_origin_y - radius,
#         circle_origin_x,
#         circle_origin_y + radius,
#         fill="black",
#         width="1",
#     )


# def draw_theta_text(
#     main_line_midpoint_x,
#     main_line_midpoint_y,
#     main_line_endpoint_x,
#     main_line_endpoint_y,
# ) -> None:
#     if main_line_endpoint_y - circle_origin_y <= 0:  # check if y endpoint is positive
#         if (
#             main_line_endpoint_x - circle_origin_x >= 0
#         ):  # check if x endpoint is positive
#             canvas.create_text(
#                 main_line_midpoint_x - 7,
#                 main_line_midpoint_y - 7,
#                 text=f"Theta : {str(args.theta)}",
#                 angle=int(args.theta),
#                 fill="green",
#                 anchor="center",
#                 # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#             )
#         else:  # check if x endpoint is negative
#             canvas.create_text(
#                 main_line_midpoint_x + 7,
#                 main_line_midpoint_y - 7,
#                 text=f"Theta : {str(args.theta)}",
#                 angle=int(args.theta) + 180,
#                 fill="green",
#                 anchor="center",
#                 # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#             )
#     else:  # check if y endpoint is negative
#         if (
#             main_line_endpoint_x - circle_origin_x >= 0
#         ):  # check if x endpont is positive
#             canvas.create_text(
#                 main_line_midpoint_x - 7,
#                 main_line_midpoint_y + 7,
#                 text=f"Theta : {str(args.theta)}",
#                 angle=int(args.theta),
#                 fill="green",
#                 anchor="center",
#                 # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#             )
#         else:  # check if x endpoint is negative
#             canvas.create_text(
#                 main_line_midpoint_x + 7,
#                 main_line_midpoint_y + 7,
#                 text=f"Theta : {str(args.theta)}",
#                 angle=int(args.theta) + 180,
#                 fill="green",
#                 anchor="center",
#                 # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#             )


# def draw_main_line_and_text() -> (
#     None
# ):  # draws main line in relation to the theta angle argument
#     # convert degrees to radians as math functions use radians
#     angle_in_radians = math.radians(int(args.theta))
#     # calculate end points with origin at center of unit circle
#     # using '-' for y-calculation if you waant 0deg=right, 90deg=up
#     x2 = circle_origin_x + main_line_length * math.cos(angle_in_radians)
#     y2 = circle_origin_y - main_line_length * math.sin(angle_in_radians)

#     print(x2)
#     print(y2)
#     # set to return value instead?
#     canvas.create_line(
#         circle_origin_x,
#         circle_origin_y,
#         x2,
#         y2,
#         fill="green",
#         width="3",
#     )

#     end_point = (x2, y2)
#     origin_point = (circle_origin_x, circle_origin_y)

#     mid_point_x = 0
#     mid_point_y = 0

#     def get_midpoint():
#         mid_point_x = (origin_point[0] + end_point[0]) / 2
#         mid_point_y = (origin_point[1] + end_point[1]) / 2

#         return mid_point_x, mid_point_y

#     mid_point_x, mid_point_y = get_midpoint()

#     # x2, y2 (endpoints)
#     # mid_point_x, mid_point_y

#     # def draw_theta_text(
#     #    main_line_midpoint_x,
#     #    main_line_midpoint_y,
#     #    main_line_endpoint_x,
#     #    main_line_endpoint_y,
#     # ) -> None:

#     def draw_main_line_theta_text(
#         main_line_endpoint_x,
#         main_line_endpoint_y,
#         main_line_midpoint_x,
#         main_line_midpoint_y,
#     ):
#         if (
#             main_line_endpoint_y - circle_origin_y <= 0
#         ):  # check if y endpoint is positive
#             if (
#                 main_line_endpoint_x - circle_origin_x >= 0
#             ):  # check if x endpoint is positive
#                 canvas.create_text(
#                     main_line_midpoint_x - 7,
#                     main_line_midpoint_y - 7,
#                     text=f"Theta : {str(args.theta)}",
#                     angle=int(args.theta),
#                     fill="green",
#                     anchor="center",
#                     # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#                 )
#             else:  # check if x endpoint is negative
#                 canvas.create_text(
#                     main_line_midpoint_x + 7,
#                     main_line_midpoint_y - 7,
#                     text=f"Theta : {str(args.theta)}",
#                     angle=int(args.theta) + 180,
#                     fill="green",
#                     anchor="center",
#                     # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#                 )
#         else:  # check if y endpoint is negative
#             if (
#                 main_line_endpoint_x - circle_origin_x >= 0
#             ):  # check if x endpont is positive
#                 canvas.create_text(
#                     main_line_midpoint_x - 7,
#                     main_line_midpoint_y + 7,
#                     text=f"Theta : {str(args.theta)}",
#                     angle=int(args.theta),
#                     fill="green",
#                     anchor="center",
#                     # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#                 )
#             else:  # check if x endpoint is negative
#                 canvas.create_text(
#                     main_line_midpoint_x + 7,
#                     main_line_midpoint_y + 7,
#                     text=f"Theta : {str(args.theta)}",
#                     angle=int(args.theta) + 180,
#                     fill="green",
#                     anchor="center",
#                     # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
#                 )

#     draw_main_line_theta_text(
#         x2, y2, mid_point_x, mid_point_y
#     )  # execute theta text function and draw theta text
#     # return x2, y2, mid_point_x, mid_point_y


# def draw_cosine_line_and_text(
#     main_line_x, main_line_y
# ) -> None:  # draws cosine line in relation to main line, and draws and aligns cosine labeling text
#     end_point = (main_line_x, circle_origin_y)
#     origin_point = (circle_origin_x, circle_origin_y)

#     mid_point_x = 0
#     mid_point_y = 0

#     def get_midpoint():
#         mid_point_x = (origin_point[0] + end_point[0]) / 2
#         mid_point_y = (origin_point[1] + end_point[1]) / 2

#         return mid_point_x, mid_point_y

#     mid_point_x, mid_point_y = get_midpoint()

#     canvas.create_line(
#         circle_origin_x,
#         circle_origin_y,
#         main_line_x,
#         circle_origin_y,
#         fill="blue",
#         width="3",
#     )
#     if (
#         main_line_y - circle_origin_y <= 0
#     ):  # if endpoint of line is above y=0 on the unit circle
#         if (
#             main_line_x - circle_origin_x >= 0
#         ):  # if endpoint of line is right of x=0 on the unit circle
#             canvas.create_text(
#                 # circle_origin_x + 5,
#                 # circle_origin_y + 5,
#                 mid_point_x,
#                 mid_point_y + 10,
#                 text="cosine of theta",
#                 fill="blue",
#                 anchor="center",
#             )
#             print(main_line_x - circle_origin_x)
#         else:  # if endpoint of line is left of x=0 on the unit circle
#             canvas.create_text(
#                 mid_point_x,
#                 mid_point_y + 10,
#                 text="cosine of theta",
#                 fill="blue",
#                 anchor="center",
#             )
#             print(main_line_x - circle_origin_x)
#     else:  # if endpoint of line is below y=0 on the unit circle
#         if (
#             main_line_x - circle_origin_x >= 0
#         ):  # if endpont of line is right of x=0 on the unit circle
#             canvas.create_text(
#                 mid_point_x,
#                 mid_point_y - 10,
#                 text="cosine of theta",
#                 fill="blue",
#                 anchor="center",
#             )
#             print(main_line_x - circle_origin_x)
#         else:  # if endpoint of line is left of x=0 on the unit circle
#             canvas.create_text(
#                 mid_point_x,
#                 mid_point_y - 10,
#                 text="cosine of theta",
#                 fill="blue",
#                 anchor="center",
#             )
#             print(main_line_x - circle_origin_x)


# def draw_sine_line_and_text(
#     main_line_x, main_line_y
# ) -> (
#     None
# ):  # draws sine line in relation to main line, and draws and aligns sine labeling text
#     end_point = (main_line_x, main_line_y)
#     origin_point = (main_line_x, circle_origin_y)
#     mid_point_x = 0
#     mid_point_y = 0

#     def get_midpoint():
#         mid_point_x = (origin_point[0] + end_point[0]) / 2
#         mid_point_y = (origin_point[1] + end_point[1]) / 2

#         return mid_point_x, mid_point_y

#     mid_point_x, mid_point_y = get_midpoint()

#     canvas.create_line(
#         main_line_x,
#         main_line_y,
#         main_line_x,
#         circle_origin_y,
#         fill="red",
#         width="3",
#     )
#     # print sin of theta on right side
#     if main_line_x - circle_origin_x >= 0:
#         canvas.create_text(
#             mid_point_x + 5,
#             mid_point_y,
#             text="sine of theta",
#             fill="red",
#             anchor="w",
#         )
#         print(main_line_x - circle_origin_x)
#     # print sin of theta on left side
#     else:
#         canvas.create_text(
#             mid_point_x - 5,
#             mid_point_y,
#             text="sine of theta",
#             fill="red",
#             anchor="e",
#         )
#         print(main_line_x - circle_origin_x)


root = tk.Tk()
canvas = tk.Canvas(
    root, width=500, height=500, borderwidth=0, highlightthickness=0, bg="white"
)
canvas.pack(fill="both", expand=True)

unit_circle = ucc.Unit_circle(canvas, args.theta)
unit_circle.draw()

# unit_circle.draw_title()
# unit_circle.draw_unit_circle()
# unit_circle.draw_x_line()
# unit_circle.draw_y_line()
# unit_circle.draw_main_line_and_theta_text()
# unit_circle.draw_cosine_line_and_text()
# unit_circle.draw_sine_line_and_text()

# draw_title()
# draw_unit_circle()
# draw_x_line()
# draw_y_line()
# draw_main_line_and_text()
# draw_cosine_line_and_text(main_line_endpoint_x, main_line_endpoint_y)
# draw_sine_line_and_text(main_line_endpoint_x, main_line_endpoint_y)
# print("TEST TEXT FOR GITHUB UPLOAD")

root.mainloop()
