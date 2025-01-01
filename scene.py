from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        integrals_text = Text(
            "What the hell are integrals?", 
            t2c={'[17:27]': BLUE}
            )

        derivatives_text = Text(
            "What the hell are derivatives?",
            t2c={'[17:29]': BLUE}
            )

        # Create ValueTrackers for dynamic range
        x_range = ValueTracker(5)
        y_range = ValueTracker(5)

        # Create the axes that will always update based on the ValueTrackers
        axes = always_redraw(lambda: Axes(
            x_range=(0, x_range.get_value()),  # Use ValueTracker for dynamic range
            x_length=13,
            y_range=(0, y_range.get_value()),  # Use ValueTracker for dynamic range
            y_length=7,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 24}
        ))
        
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        axis_labels[0].set_font_size(36)
        axis_labels[1].set_font_size(36)

        # Groups axis elements into one
        axes_group = VGroup(axes, axis_labels)

        x_squared = axes.plot(
            lambda x: x**2, 
            color=RED, 
            x_range=[0, x_range.get_value()]
            )

        points = [
            [1, 1, 0],
            [2, 4, 0]
        ]

        # Converts original coordinates to axes coordinates
        dots = VGroup(*[Dot(axes.c2p(p[0], p[1])) for p in points])
        dots.set_color(color=RED)
        dot_positions = VGroup(*[
            Text(f"({p[0]}, {p[1]})")
            .scale(0.4)
            .next_to(dots[i], RIGHT)
            for i, p in enumerate(points)])
        dot_positions.set_color(color=RED)
        

        self.play(
            Write(integrals_text),
            run_time=3,
            rate_func=rate_functions.ease_in_out_cubic
        )
        self.wait(2)

        self.play(
            Transform(integrals_text, derivatives_text),
            run_time=3
            )
        
        self.wait(2)

        self.play(Unwrite(integrals_text), run_time=1)

        self.wait(1)

        self.play(
            FadeIn(axes_group),
            run_time=2,
            rate_func=rate_functions.ease_in_out_cubic
        )

        self.wait(1)

        self.play(
            Write(x_squared),
            run_time=2,
            rate_func=rate_functions.ease_in_out_cubic,
        )

        self.play(Write(dots), 
                  Write(dot_positions),
        )

        self.wait(3)

        connecting_dot = Dot(axes.c2p(1, 4, 0), color=RED)
        self.play(FadeIn(connecting_dot), run_time=2)

        # Creates a line connecting the points
        points.insert(1, [1, 4, 0])
        transformed_points = [axes.c2p(x, y, z) for x, y, z in points]
        rise_run = VMobject()
        rise_run.set_points_as_corners(transformed_points)
        rise_run.set_color(color=RED)

        self.play(
            Create(rise_run),
            run_time=3,
            rate_func=rate_functions.ease_in_out_cubic
            )
        
        rise_num = Text("4", font_size=36)
        run_num = Text("1", font_size=36)
        rise_num.next_to(rise_run, LEFT)
        run_num.next_to(rise_run, UP)
        rr_num = VGroup(rise_num, run_num)

        self.play(Write(rise_num))
        self.play(Write(run_num))

        self.wait(2)

        wrong_slope = Text(
            "Slope = 4?", 
            font_size=72, 
            color=YELLOW_D
        )
        wrong_slope.shift(RIGHT*2)

        self.play(
            Transform(rr_num, wrong_slope),
            run_time=2,
            rate_func=rate_functions.ease_in_out_cubic
        )

        self.play(
            FadeOut(rr_num), 
            FadeOut(rise_run),
            FadeOut(dots),
            FadeOut(dot_positions),
            FadeOut(connecting_dot)
            )

        self.play(
            x_range.animate.set_value(10), 
            y_range.animate.set_value(10)
        )

        axes_two = Axes(
            x_range=(0, 10), 
            x_length=13,
            y_range=(0, 10),
            y_length=7,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 24}
        )

        x_squared_two = axes_two.plot(lambda x: x**2, color=RED)

        self.play(Transform(x_squared, x_squared_two))
    
        self.wait(3)