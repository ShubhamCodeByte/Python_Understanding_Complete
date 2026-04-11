"""
5. Write a class vector representing a vector of n dimensions. Overload the + and *
operator which calculates the sum and the dot(.) product of them.

"""


class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.dims = len(coordinates)

    def __add__(self, other):
        # Ensure dimensions match
        if self.dims != other.dims:
            raise ValueError("Vectors must have the same dimensions for addition.")
        
        # Add corresponding elements: (a1+b1, a2+b2, ...)
        new_coords = [self.coordinates[i] + other.coordinates[i] for i in range(self.dims)]
        return Vector(new_coords)

    def __mul__(self, other):
        # Ensure dimensions match
        if self.dims != other.dims:
            raise ValueError("Vectors must have the same dimensions for dot product.")
        
        # Dot product: (a1*b1 + a2*b2 + ...)
        # We sum the products of corresponding elements
        dot_product = sum(self.coordinates[i] * other.coordinates[i] for i in range(self.dims))
        return dot_product

    def __str__(self):
        return f"Vector({self.coordinates})"

# --- Testing the Class ---
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

v_sum = v1 + v2
v_dot = v1 * v2

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"Sum: {v_sum}")    # Expected: Vector([5, 7, 9])
print(f"Dot Product: {v_dot}") # Expected: (1*4 + 2*5 + 3*6) = 4 + 10 + 18 = 32