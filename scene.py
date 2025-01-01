from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        integrals_text = Text("What the hell are integrals?")
        integrals_text[14:23].set_color(color=BLUE)

        derivatives_text = Text("What the hell are derivatives?")
        derivatives_text[14:25].set_color(color=BLUE)

        # x_length = 14.2, y_length = 8 are full screen axes
        axes = Axes(
            x_range=(0, 5), 
            x_length=13, 
            y_range=(0,5), 
            y_length=7, 
            tips=False,
            axis_config={"include_numbers": True,
                         "font_size": 24}
            )
        
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        axis_labels[0].set_font_size(36)
        axis_labels[1].set_font_size(36)

        axes_group = VGroup(axes, axis_labels)
        x_squared = axes.plot(lambda x: x**2, color=RED)
        points = [
            [1, 1],
            [2, 4]
        ]

        dots = VGroup(*[Dot(axes.c2p(p[0], p[1])) for p in points])
        dot_positions = VGroup(*[
            Text(f"({p[0]}, {p[1]})")
            .scale(0.4)  # Scale down the text
            .next_to(dots[i], UP)  # Position text above the dot
            for i, p in enumerate(points)])

        self.play(
            Write(integrals_text),
            run_time=3,
            rate_func=rate_functions.ease_in_out_cubic
        )
        self.wait(2)

        self.play(
            Transform(integrals_text, derivatives_text),
            run_time=2
            )
        
        self.wait(2)

        self.play(
            Transform(integrals_text, axes_group),
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

        self.wait(5)