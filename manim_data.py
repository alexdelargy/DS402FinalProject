from manim import *

class DataTableScene(Scene):
    def construct(self):
        data = [
            [
                'InvoiceNo',
                'StockCode',
                'Description',
                'Quantity',
                'InvoiceDate',
                'UnitPrice',
                'CustomerID',
                'Country'
            ],
            [
                'String',
                'String',
                'String',
                'Int',
                'String',
                'Float',
                'Float',
                'String'
            ]
        ]

        # Function to create each cell with a background rectangle and text
        def create_cell(content, width, height, bg_color=WHITE, text_color=BLACK, bold=False):
            rect = Rectangle(width=width, height=height, fill_color=bg_color, fill_opacity=1, stroke_width=1)
            text = Text(content, font_size=24, color=text_color, font="Arial", weight=BOLD if bold else NORMAL)
            text.set_max_width(width - 0.1)
            text.move_to(rect.get_center())
            cell = VGroup(rect, text)
            return cell

        # Determine cell dimensions
        cell_width = 2  # Adjust as needed
        cell_height = 0.8  # Adjust as needed

        # Create table cells
        table_rows = []
        for row_index, row_data in enumerate(data):
            table_row = VGroup()
            for col_index, cell_content in enumerate(row_data):
                if row_index == 0:
                    # Header row styling
                    bg_color = BLUE_E
                    text_color = WHITE
                    bold = True
                elif row_index % 2 == 1:
                    # Alternating row colors
                    bg_color = GRAY_A
                    text_color = BLACK
                    bold = False
                else:
                    bg_color = WHITE
                    text_color = BLACK
                    bold = False
                cell = create_cell(cell_content, cell_width, cell_height, bg_color, text_color, bold)
                cell.shift(RIGHT * col_index * cell_width)
                table_row.add(cell)
            table_row.shift(DOWN * row_index * cell_height)
            table_rows.append(table_row)

        # Group all table rows
        table = VGroup(*table_rows)
        table.move_to(ORIGIN)
        table.scale_to_fit_width(config.frame_width - 1)

        # Animate the table
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=DOWN) for row in table_rows],
                lag_ratio=0.1
            )
        )
        self.wait(10)
