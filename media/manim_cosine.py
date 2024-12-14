from manim import *
import numpy as np


class CosineSimilarity3D(ThreeDScene):
    def construct(self):
        # Set up 2D axes
        axes = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[-1, 1, 0.5],
            axis_config={"include_numbers": True},
            x_length=6,
            y_length=6
        )
        axes_labels = axes.get_axis_labels(
            x_label="x", y_label="y"
        )

        # 3D Camera setup
        self.set_camera_orientation(phi=0 * DEGREES, theta=270 * DEGREES)
        self.play(Create(axes), Write(axes_labels))

        # Define first set of vectors
        vector_a = np.array([0.8, 0.6])  # Current vector 1
        vector_b = np.array([0.4, 0.9])  # Current vector 2

        vec_a = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*vector_a),
            color=BLUE,
            stroke_width=4,
        )
        vec_b = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*vector_b),
            color=GREEN,
            stroke_width=4,
        )

        # Add labels for vectors
        label_a = MathTex("\\vec{a}", color=BLUE).next_to(vec_a.get_end(), RIGHT)
        label_b = MathTex("\\vec{b}", color=GREEN).next_to(vec_b.get_end(), UP)

        self.play(Create(vec_a), Write(label_a))
        self.play(Create(vec_b), Write(label_b))

        # Display the angle arc between vectors
        angle_arc = Angle(
            vec_a,
            vec_b,
            other_angle=False,
            radius=1,
            color=YELLOW,
        )
        self.play(Create(angle_arc))

        # Calculate and display angle
        dot_product = np.dot(vector_a, vector_b)
        magnitude_a = np.linalg.norm(vector_a)
        magnitude_b = np.linalg.norm(vector_b)
        cosine_theta = dot_product / (magnitude_a * magnitude_b)
        angle_radians = np.arccos(cosine_theta)
        angle_degrees = np.degrees(angle_radians)

        angle_text = MathTex(f"\\theta \\approx {angle_degrees:.2f}^\\circ").move_to([3, 3, 0])
        cosine_text = MathTex(f"\\cos(\\theta) \\approx {cosine_theta:.2f}").next_to(angle_text, DOWN)
        self.play(Write(angle_text), Write(cosine_text))

        # Pause for a moment
        self.wait(10)

        # Remove first set of vectors
        self.play(FadeOut(vec_a), FadeOut(cosine_text), FadeOut(label_b), FadeOut(vec_b), FadeOut(angle_arc), FadeOut(angle_text))

        # Add smaller angle vector
        vector_c = np.array([0.9, 0.3])  # New vector with a smaller angle
        vec_c = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*vector_c),
            color=ORANGE,
            stroke_width=4,
        )

        # Label and arc for smaller angle
        label_a = MathTex("\\vec{a}", color=BLUE).next_to(vec_a.get_end(), RIGHT)
        label_c = MathTex("\\vec{b}", color=ORANGE).next_to(vec_c.get_end(), RIGHT)

        self.play(Create(vec_a), Write(label_a))
        self.play(Create(vec_c), Write(label_c))

        smaller_angle_arc = Angle(
            vec_a,
            vec_c,
            other_angle=True,
            radius=1,
            color=YELLOW,
        )
        self.play(Create(smaller_angle_arc))

        # Calculate and display smaller angle
        dot_product_small = np.dot(vector_a, vector_c)
        cosine_theta_small = dot_product_small / (magnitude_a * np.linalg.norm(vector_c))
        angle_radians_small = np.arccos(cosine_theta_small)
        angle_degrees_small = np.degrees(angle_radians_small)

        smaller_angle_text = MathTex(f"\\theta \\approx {angle_degrees_small:.2f}^\\circ").move_to([3, 3, 0])
        cosine_text_small = MathTex(f"\\cos(\\theta) \\approx {cosine_theta_small:.2f}").next_to(smaller_angle_text, DOWN)
        self.play(Write(smaller_angle_text), Write(cosine_text_small))

        self.wait(10)

        # Remove smaller angle vectors
        self.play(FadeOut(vec_c), FadeOut(cosine_text_small), FadeOut(label_c), FadeOut(smaller_angle_arc), FadeOut(smaller_angle_text))

        # Add larger angle vector
        vector_d = np.array([-0.5, 0.8])  # New vector with a larger angle
        vec_d = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(*vector_d),
            color=PURPLE,
            stroke_width=4,
        )

        # Label and arc for larger angle
        label_a = MathTex("\\vec{a}", color=BLUE).next_to(vec_a.get_end(), RIGHT)
        label_d = MathTex("\\vec{b}", color=PURPLE).next_to(vec_d.get_end(), UP)

        self.play(Create(vec_a), Write(label_a))
        self.play(Create(vec_d), Write(label_d))

        larger_angle_arc = Angle(
            vec_a,
            vec_d,
            other_angle=False,
            radius=1,
            color=YELLOW,
        )
        self.play(Create(larger_angle_arc))

        # Calculate and display larger angle
        dot_product_large = np.dot(vector_a, vector_d)
        cosine_theta_large = dot_product_large / (magnitude_a * np.linalg.norm(vector_d))
        angle_radians_large = np.arccos(cosine_theta_large)
        angle_degrees_large = np.degrees(angle_radians_large)

        larger_angle_text = MathTex(f"\\theta \\approx {angle_degrees_large:.2f}^\\circ").move_to([2, 3, 0])
        cosine_text_large = MathTex(f"\\cos(\\theta) \\approx {cosine_theta_large:.2f}").next_to(larger_angle_text, DOWN)
        self.play(Write(larger_angle_text), Write(cosine_text_large))

        self.wait(10)

    

scene = CosineSimilarity3D()
scene.construct()