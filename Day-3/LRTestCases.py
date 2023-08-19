# Numpy for linear algebra and mathematical functions
import numpy as np

# Color for messages
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Function to test `euclidean_distance_3d` function
def test_euclidean_distance_3d(incomplete_euclidean_distance_3d, point_a, point_b):
    # Function to caluclate euclidean distance
    def correct_euclidean_distance_3d(point_1, point_2):
        # Extract x, y and z value from each point
        x1, y1, z1 = point_a
        x2, y2, z2 = point_b
    
        # Now we apply the formula for euclidean distance
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    
        # Return the distance
        return distance

    # Get the answer from the `incomplete_euclidean_distance_3d` function
    if incomplete_euclidean_distance_3d(point_a, point_b) == correct_euclidean_distance_3d(point_a, point_b):
        print(GREEN + "Test passed!" + RESET)
    else:
        print(RED + "Error! Test Failed!" + RESET)


# Function to test `euclidean_distance_2d` function
def test_euclidean_distance_2d(incomplete_euclidean_distance_2d, point_a, point_b):
    # Function to caluclate euclidean distance
    def correct_euclidean_distance_2d(point_1, point_2):
        # Extract x and y value from each point
        x1, y1 = point_a
        x2, y2 = point_b
    
        # Now we apply the formula for euclidean distance
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
        # Return the distance
        return distance

    # Get the answer from the `incomplete_euclidean_distance_2d` function
    if incomplete_euclidean_distance_2d(point_a, point_b) == correct_euclidean_distance_2d(point_a, point_b):
        print(GREEN + "Test passed!" + RESET)
    else:
        print(RED + "Error! Test Failed!" + RESET)


# Function to test `manhattan_distance_3d` function
def test_manhattan_distance_3d(incomplete_manhattan_distance_3d, point_a, point_b):
    # Function to caluclate manhattan distance
    def correct_manhattan_distance_3d(point_1, point_2):
        # Extract x, y and z value from each point
        x1, y1, z1 = point_a
        x2, y2, z2 = point_b
    
        # Now we apply the formula for manhattan distance
        distance = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
    
        # Return the distance
        return distance

    # Get the answer from the `incomplete_manhattan_distance_3d` function
    if incomplete_manhattan_distance_3d(point_a, point_b) == correct_manhattan_distance_3d(point_a, point_b):
        print(GREEN + "Test passed!" + RESET)
    else:
        print(RED + "Error! Test Failed!" + RESET)


# Function to test `manhattan_distance_2d` function
def test_manhattan_distance_2d(incomplete_manhattan_distance_2d, point_a, point_b):
    # Function to caluclate manhattan distance
    def correct_manhattan_distance_2d(point_1, point_2):
        # Extract x and y value from each point
        x1, y1 = point_a
        x2, y2 = point_b
    
        # Now we apply the formula for manhattan distance
        distance = abs(x2 - x1) + abs(y2 - y1)
    
        # Return the distance
        return distance

    # Get the answer from the `incomplete_manhattan_distance_2d` function
    if incomplete_manhattan_distance_2d(point_a, point_b) == correct_manhattan_distance_2d(point_a, point_b):
        print(GREEN + "Test passed!" + RESET)
    else:
        print(RED + "Error! Test Failed!" + RESET)


# Function to test `cosine_similarity` function
def test_cosine_similarity(incomplete_cosine_similarity, vector1, vector2):
    # Function to calculate cosine similarity
    def correct_cosine_similarity(vector1, vector2):
        # Get the dot of vectors -> Numerator
        dot_product = np.dot(vector1, vector2)
    
        # Calculate magnitude for each vector
        magnitude1 = np.linalg.norm(vector1)
        magnitude2 = np.linalg.norm(vector2)
    
        # Get the product of magnitude -> Denominator
        magnitude_product = magnitude1 * magnitude2
    
        # Calculate the similarity
        similarity = dot_product / magnitude_product
    
        # Return the similarity value
        return similarity

    # Get the answer from the `incomplete_manhattan_distance_2d` function
    if incomplete_cosine_similarity(vector1, vector2) == correct_cosine_similarity(vector1, vector2):
        print(GREEN + "Test passed!" + RESET)
    else:
        print(RED + "Error! Test Failed!" + RESET)