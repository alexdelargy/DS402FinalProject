from manim import *

class OneHotEncoding(Scene):
    def construct(self):
        # Sample dataset
        data = [
            ["customerID", "productID"],
            ["C001", "P1"],
            ["C002", "P2"],
            ["C003", "P1"],
            ["C004", "P3"],
            ["C005", "P2"],
            ["C006", "P1"],
        ]

        # Create initial table
        initial_table = Table(
            data,
            include_outer_lines=True,
            h_buff=0.6,
            v_buff=0.3,
        ).scale(0.6).move_to([-4, 0, 0])

        # Display the initial table
        self.play(Write(initial_table))
        self.wait(1)

        # Highlight the 'productID' column
        product_col = initial_table.get_columns()[1]
        product_col_rect = SurroundingRectangle(product_col, color=YELLOW, buff=0.05)
        self.play(Create(product_col_rect))
        self.wait(1)

        # Extract unique products
        products = sorted(set(row[1] for row in data[1:]))

        # Build new data with one-hot encoding
        new_data = [["customerID"] + products]
        for row in data[1:]:
            customerID = row[0]
            productID = row[1]
            one_hot = ["1" if product == productID else "0" for product in products]
            new_data.append([customerID] + one_hot)

        # Create the new table
        new_table = Table(
            new_data,
            include_outer_lines=True,
            h_buff=0.6,
            v_buff=0.3,
        ).scale(0.6)

        # Position the new table to the right
        new_table.next_to(initial_table, RIGHT, buff=0.5)

        # Draw an arrow from the 'productID' column to the new columns
        arrow = Arrow(
            product_col.get_right(),
            new_table.get_left(),
            buff=0.1,
            color=WHITE
        )
        self.play(GrowArrow(arrow))
        self.wait(1)

        # Display the new table
        self.play(Write(new_table))
        self.wait(1)

        # Clean up
        self.play(FadeOut(product_col_rect), FadeOut(arrow))
        self.wait(1)

        # Highlight a row in the new table (e.g., customer 'C001')
        selected_row_index = 1  # Index of 'C001' in new_data (excluding header)
        selected_row = new_table.get_rows()[selected_row_index]
        row_rect = SurroundingRectangle(selected_row, color=BLUE, buff=0.05)
        self.play(Create(row_rect))
        self.wait(1)

        # Extract the data from the selected row (excluding 'customerID')
        vector_data = new_data[selected_row_index][1:]  # Exclude 'customerID' column

        # Get the table entries for the selected row (excluding 'customerID')
        entry_mobjects = [
            new_table.get_cell((selected_row_index + 1, col)).copy()
            for col in range(2, len(products) + 2)
        ]

        # Create vector entries
        vector_entries = VGroup(
            *[MathTex(number).scale(1) for number in vector_data]
        ).arrange(RIGHT, aligned_edge=LEFT)

        # Position the vector entries below the new table
        vector_entries.next_to(new_table, RIGHT, buff=0.5)

        # Create brackets
        left_bracket = MathTex(r"\left[")
        right_bracket = MathTex(r"\right]")

        # Position brackets
        left_bracket.next_to(vector_entries, LEFT, buff=0.1)
        right_bracket.next_to(vector_entries, RIGHT, buff=0.1)

        # Group vector components
        vector_group = VGroup(left_bracket, vector_entries, right_bracket)

        # Animate the transformation from table entries to vector entries
        self.play(
            *[
                TransformFromCopy(entry_mobjects[i], vector_entries[i])
                for i in range(len(vector_entries))
            ],
            Write(left_bracket),
            Write(right_bracket)
        )
        self.wait(2)


        selected_row_index_2 = 2  # Index of 'C001' in new_data (excluding header)
        selected_row_2 = new_table.get_rows()[selected_row_index_2]
        row_rect_2 = SurroundingRectangle(selected_row_2, color=BLUE, buff=0.05)
        self.play(Create(row_rect_2))
        self.wait(1)

        # Extract the data from the selected row (excluding 'customerID')
        vector_data_2 = new_data[selected_row_index_2][1:]  # Exclude 'customerID' column

        # Get the table entries for the selected row (excluding 'customerID')
        entry_mobjects_2 = [
            new_table.get_cell((selected_row_index_2 + 1, col)).copy()
            for col in range(2, len(products) + 2)
        ]

        # Create vector entries
        vector_entries_2 = VGroup(
            *[MathTex(number).scale(1) for number in vector_data_2]
        ).arrange(RIGHT, aligned_edge=LEFT)

        # Position the vector entries below the new table
        vector_entries_2.next_to(new_table, RIGHT, buff=0.5).shift(DOWN * 1)

        # Create brackets
        left_bracket_2 = MathTex(r"\left[")
        right_bracket_2 = MathTex(r"\right]")

        # Position brackets
        left_bracket_2.next_to(vector_entries_2, LEFT, buff=0.1)
        right_bracket_2.next_to(vector_entries_2, RIGHT, buff=0.1)

        # Group vector components
        vector_group_2 = VGroup(left_bracket_2, vector_entries_2, right_bracket_2)

        # Animate the transformation from table entries to vector entries
        self.play(
            *[
                TransformFromCopy(entry_mobjects_2[i], vector_entries_2[i])
                for i in range(len(vector_entries_2))
            ],
            Write(left_bracket_2),
            Write(right_bracket_2)
        )
        self.wait(5)

OneHotEncoding().construct()