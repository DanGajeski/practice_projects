import math
import tkinter as tk


class Unit_circle:
    def __init__(self, canvas, theta):  # pass in created tk.canvas
        self.canvas = canvas
        self.theta = theta  # current theta
        self.circle_origin_x = 250
        self.circle_origin_y = 250
        self.title_y_location = 50
        self.title_x_location = self.circle_origin_x
        self.radius = 100
        self.main_line_length = self.radius  # redundant?
        # used for cos line
        self.main_line_endpoint_x = 0
        # used for sin line
        self.main_line_endpoint_y = 0

        self.theta_slider = self.create_slider()
        self.theta_slider_value = (
            self.theta_slider.get()
        )  # get initial value of theta slider

        # create slider window and slider scale object to modify theta values
        self.create_slider_window()

    def draw_title(self) -> None:  # draws title text centered
        self.canvas.create_text(
            self.title_x_location,
            self.title_y_location,
            text="The Unit Circle\nPlotting Sine and Cosine",
            font=("Arial", 25, "bold"),
            justify="center",
            fill="black",
            anchor="center",
            tags=("title_tag"),
        )

    def draw_unit_circle(self) -> None:  # draws main unit circle
        self.canvas.create_oval(
            self.circle_origin_x - self.radius,
            self.circle_origin_y - self.radius,
            self.circle_origin_x + self.radius,
            self.circle_origin_y + self.radius,
            fill="white",
            outline="black",
            width=2,
            tags=("unit_circle_tag"),
        )

    def draw_x_line(self) -> None:  # draws unit circle x line
        self.canvas.create_line(
            self.circle_origin_x - self.radius,
            self.circle_origin_y,
            self.circle_origin_x + self.radius,
            self.circle_origin_y,
            fill="black",
            width="1",
            tags=("x_line_tag"),
        )

    def draw_y_line(self) -> None:  # draws unit circle y line
        self.canvas.create_line(
            self.circle_origin_x,
            self.circle_origin_y - self.radius,
            self.circle_origin_x,
            self.circle_origin_y + self.radius,
            fill="black",
            width="1",
            tags=("y_line_tag"),
        )

    def draw_main_line_and_theta_text(
        self,
    ) -> None:  # draws main line in relation to the theta angle argument
        # convert degrees to radians as math functions use radians
        angle_in_radians = math.radians(int(self.theta))
        # calculate end points with origin at center of unit circle
        # using '-' for y-calculation if you waant 0deg=right, 90deg=up
        self.main_line_endpoint_x = (
            self.circle_origin_x + self.main_line_length * math.cos(angle_in_radians)
        )  # used in drawing theta text
        self.main_line_endpoint_y = (
            self.circle_origin_y - self.main_line_length * math.sin(angle_in_radians)
        )  # used in drawing theta text

        # set to return value instead?
        self.canvas.create_line(
            self.circle_origin_x,
            self.circle_origin_y,
            self.main_line_endpoint_x,
            self.main_line_endpoint_y,
            fill="green",
            width="3",
            tags=("main_line_tag"),
        )

        end_point = (self.main_line_endpoint_x, self.main_line_endpoint_y)
        origin_point = (self.circle_origin_x, self.circle_origin_y)

        mid_point_x = 0  # used in drawing theta text
        mid_point_y = 0  # used in drawing theta text

        def get_midpoint():
            mid_point_x = (origin_point[0] + end_point[0]) / 2
            mid_point_y = (origin_point[1] + end_point[1]) / 2

            return mid_point_x, mid_point_y

        mid_point_x, mid_point_y = get_midpoint()  # used in drawing theta text

        # x2, y2 (endpoints)
        # mid_point_x, mid_point_y

        # def draw_theta_text(
        #    main_line_midpoint_x,
        #    main_line_midpoint_y,
        #    main_line_endpoint_x,
        #    main_line_endpoint_y,
        # ) -> None:

        def draw_main_line_theta_text(main_line_midpoint_x, main_line_midpoint_y):
            if (
                self.main_line_endpoint_y - self.circle_origin_y <= 0
            ):  # check if y endpoint is positive
                if (
                    self.main_line_endpoint_x - self.circle_origin_x >= 0
                ):  # check if x endpoint is positive
                    self.canvas.create_text(
                        main_line_midpoint_x - 7,
                        main_line_midpoint_y - 7,
                        text=f"Theta : {str(self.theta)}",
                        angle=int(self.theta),
                        fill="green",
                        anchor="center",
                        tags=("theta_text_tag"),
                        # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
                    )
                else:  # check if x endpoint is negative
                    self.canvas.create_text(
                        main_line_midpoint_x + 7,
                        main_line_midpoint_y - 7,
                        text=f"Theta : {str(self.theta)}",
                        angle=int(self.theta) + 180,
                        fill="green",
                        anchor="center",
                        tags=("theta_text_tag"),
                        # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
                    )
            else:  # check if y endpoint is negative
                if (
                    self.main_line_endpoint_x - self.circle_origin_x >= 0
                ):  # check if x endpont is positive
                    self.canvas.create_text(
                        main_line_midpoint_x - 7,
                        main_line_midpoint_y + 7,
                        text=f"Theta : {str(self.theta)}",
                        angle=int(self.theta),
                        fill="green",
                        anchor="center",
                        tags=("theta_text_tag"),
                        # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
                    )
                else:  # check if x endpoint is negative
                    self.canvas.create_text(
                        main_line_midpoint_x + 7,
                        main_line_midpoint_y + 7,
                        text=f"Theta : {str(self.theta)}",
                        angle=int(self.theta) + 180,
                        fill="green",
                        anchor="center",
                        tags=("theta_text_tag"),
                        # canvas.create_text(200, 200, text="Rotated Text", angle=45, font=("Arial", 20))
                    )

        draw_main_line_theta_text(
            mid_point_x, mid_point_y
        )  # execute theta text function and draw theta text
        # return x2, y2, mid_point_x, mid_point_y
        #

    def draw_cosine_line_and_text(
        self,
    ) -> None:  # draws cosine line in relation to main line, and draws and aligns cosine labeling text
        end_point = (self.main_line_endpoint_x, self.circle_origin_y)
        origin_point = (self.circle_origin_x, self.circle_origin_y)

        mid_point_x = 0
        mid_point_y = 0

        def get_midpoint():
            mid_point_x = (origin_point[0] + end_point[0]) / 2
            mid_point_y = (origin_point[1] + end_point[1]) / 2

            return mid_point_x, mid_point_y

        mid_point_x, mid_point_y = get_midpoint()

        self.canvas.create_line(
            self.circle_origin_x,
            self.circle_origin_y,
            self.main_line_endpoint_x,
            self.circle_origin_y,
            fill="blue",
            width="3",
            tags=("cosine_line_tag"),
        )
        if (
            self.main_line_endpoint_y - self.circle_origin_y <= 0
        ):  # if endpoint of line is above y=0 on the unit circle
            if (
                self.main_line_endpoint_x - self.circle_origin_x >= 0
            ):  # if endpoint of line is right of x=0 on the unit circle
                self.canvas.create_text(
                    # circle_origin_x + 5,
                    # circle_origin_y + 5,
                    mid_point_x,
                    mid_point_y + 10,
                    text="cosine of theta",
                    fill="blue",
                    anchor="center",
                    tags=("cosine_text_tag"),
                )
                # print(main_line_x - circle_origin_x)
            else:  # if endpoint of line is left of x=0 on the unit circle
                self.canvas.create_text(
                    mid_point_x,
                    mid_point_y + 10,
                    text="cosine of theta",
                    fill="blue",
                    anchor="center",
                    tags=("cosine_text_tag"),
                )
                # print(main_line_x - circle_origin_x)
        else:  # if endpoint of line is below y=0 on the unit circle
            if (
                self.main_line_endpoint_x - self.circle_origin_x >= 0
            ):  # if endpont of line is right of x=0 on the unit circle
                self.canvas.create_text(
                    mid_point_x,
                    mid_point_y - 10,
                    text="cosine of theta",
                    fill="blue",
                    anchor="center",
                    tags=("cosine_text_tag"),
                )
                # print(main_line_x - circle_origin_x)
            else:  # if endpoint of line is left of x=0 on the unit circle
                self.canvas.create_text(
                    mid_point_x,
                    mid_point_y - 10,
                    text="cosine of theta",
                    fill="blue",
                    anchor="center",
                    tags=("cosine_text_tag"),
                )
                # print(main_line_x - circle_origin_x)

    def draw_sine_line_and_text(
        self,
    ) -> None:  # draws sine line in relation to main line, and draws and aligns sine labeling text
        end_point = (self.main_line_endpoint_x, self.main_line_endpoint_y)
        origin_point = (self.main_line_endpoint_x, self.circle_origin_y)
        mid_point_x = 0
        mid_point_y = 0

        def get_midpoint():
            mid_point_x = (origin_point[0] + end_point[0]) / 2
            mid_point_y = (origin_point[1] + end_point[1]) / 2

            return mid_point_x, mid_point_y

        mid_point_x, mid_point_y = get_midpoint()

        self.canvas.create_line(
            self.main_line_endpoint_x,
            self.main_line_endpoint_y,
            self.main_line_endpoint_x,
            self.circle_origin_y,
            fill="red",
            width="3",
            tags=("sine_text_tag"),
        )
        # print sin of theta on right side
        if self.main_line_endpoint_x - self.circle_origin_x >= 0:
            self.canvas.create_text(
                mid_point_x + 5,
                mid_point_y,
                text="sine of theta",
                fill="red",
                anchor="w",
                tags=("sine_text_tag"),
            )
            # print(main_line_x - circle_origin_x)
        # print sin of theta on left side
        else:
            self.canvas.create_text(
                mid_point_x - 5,
                mid_point_y,
                text="sine of theta",
                fill="red",
                anchor="e",
                tags=("sine_text_tag"),
            )
            # print(main_line_x - circle_origin_x)

    # def update_unit_circle_theta(self):
    #    self.theta = self.theta_slider.get()

    # INIT function
    def create_slider(self):
        # 2. Create the Slider (Scale widget)
        # Set its parent as the canvas or root
        theta_slider = tk.Scale(
            self.canvas,
            from_=0,
            to=360,
            orient="horizontal",
            length=360,
            command=self.on_slider_move,
        )
        theta_slider.set(self.theta)  # set initial slider value to user inputted theta

        return theta_slider

    # INIT function
    def create_slider_window(self):
        # 3. Embed the Slider into the Canvas
        # This places the slider widget at the specified (x, y) coordinates
        self.canvas.create_window(
            self.circle_origin_x,
            self.circle_origin_y + self.radius + 50,
            window=self.theta_slider,
            anchor="center",
        )

    def on_slider_move(self, slider_value):
        self.theta = slider_value
        print(self.theta)
        self.canvas.delete("title_tag")
        self.canvas.delete("unit_circle_tag")
        self.canvas.delete("x_line_tag")
        self.canvas.delete("y_line_tag")
        self.canvas.delete("main_line_tag")
        self.canvas.delete("theta_text_tag")
        self.canvas.delete("cosine_line_tag")
        self.canvas.delete("cosine_text_tag")
        self.canvas.delete("sine_line_tag")
        self.canvas.delete("sine_text_tag")
        self.draw()

    def draw(self):
        self.draw_title()
        self.draw_unit_circle()
        self.draw_x_line()
        self.draw_y_line()
        self.draw_main_line_and_theta_text()
        self.draw_cosine_line_and_text()
        self.draw_sine_line_and_text()
        # self.draw_slider()
