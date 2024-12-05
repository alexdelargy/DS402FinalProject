from manim import *
import pandas as pd
import numpy as np

# Example customer similarity matrix and product recommendations
data = {
    'Customer1': [1.0, 0.9, 0.7, 0.2],
    'Customer2': [0.9, 1.0, 0.4, 0.1],
    'Customer3': [0.7, 0.4, 1.0, 0.3],
    'Customer4': [0.2, 0.1, 0.3, 1.0]
}

similarities_df = pd.DataFrame(data, index=['Customer1', 'Customer2', 'Customer3', 'Customer4'])
recommended_products = {
    'Customer1': ['Product A', 'Product B'],
    'Customer2': ['Product C'],
    'Customer3': ['Product D', 'Product E'],
    'Customer4': ['Product A']
}

class CustomerSimilaritiesVisualization(Scene):
    def construct(self):
        # Create a table for the customer similarity matrix
        similarity_matrix_table = Table(
            [["{:.1f}".format(similarities_df.iloc[i, j]) for j in range(similarities_df.shape[1])] for i in range(similarities_df.shape[0])],
            row_labels=[Text(customer) for customer in similarities_df.index],
            col_labels=[Text(customer) for customer in similarities_df.columns],
            top_left_entry=Text("Similarity"),
            include_outer_lines=True
        ).scale(0.5)

        # Add the similarity matrix table to the scene
        self.play(Create(similarity_matrix_table))
        self.wait(2)

        # Highlight the most similar customer for Customer1
        most_similar_customer = np.argmax(similarities_df.loc['Customer1'][1:]) + 1  # Exclude self-similarity
        highlight_rect = similarity_matrix_table.get_highlighted_cell((3, 2), color=YELLOW)

        # Highlight the similarity score
        self.play(Create(highlight_rect))
        self.wait(5)

# To render this scene, save the file as `customer_similarities.py` and run the following command:
# manim -pql customer_similarities.py CustomerSimilaritiesVisualization
