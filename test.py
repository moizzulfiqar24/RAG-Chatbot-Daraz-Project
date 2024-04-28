# Define the initial positions mapping based on the user input, including the 'const' position
positions_with_const = {
    "const": 0,
    "p00|00": 1, "p01|00": 2, "p10|00": 3, "p11|00": 4,
    "p00|01": 5, "p01|01": 6, "p10|01": 7, "p11|01": 8,
    "p00|10": 9, "p01|10": 10, "p10|10": 11, "p11|10": 12,
    "p00|11": 13, "p01|11": 14, "p10|11": 15, "p11|11": 16
}

# The inequalities to be processed, gathered from the image provided by the user
inequalities = [
    "p00|00 + p01|00 <= p10|00 + p11|00",
    "p00|00 + p01|00 >= p10|00 + p11|00",
    "p00|01 + p01|01 <= p10|01 + p11|01",
    "p00|01 + p01|01 >= p10|01 + p11|01",
    "p01|01 + p11|01 <= p01|11 + p11|11",
    "p01|01 + p11|01 >= p01|11 + p11|11",
    "p00|10 + p01|10 <= p00|00 + p01|00",
    "p00|10 + p01|10 >= p00|00 + p01|00",
    "p01|10 + p11|10 <= p01|00 + p11|00",
    "p01|10 + p11|10 >= p01|00 + p11|00",
    "p00|11 + p01|11 <= p00|01 + p01|01",
    "p00|11 + p01|11 >= p00|01 + p01|01",
    "p01|11 + p11|11 <= p01|01 + p11|01",
    "p01|11 + p11|11 >= p01|01 + p11|01"
]

# Updated function to create array from inequality according to the new rules
def create_array_from_inequality(inequality, positions):
    array = [0] * 17  # Initialize the array with 17 positions including 'const'
    # Handle both 'greater than or equal to' and 'less than or equal to' inequalities
    if "<=" in inequality:
        lesser_side, greater_side = inequality.replace(" ", "").split("<=")
    else:
        greater_side, lesser_side = inequality.replace(" ", "").split(">=")

    # Assign 1 to the positions of elements on the greater side
    for element in greater_side.split("+"):
        if element in positions:
            array[positions[element]] = 1

    # Assign -1 to the positions of elements on the lesser side
    for element in lesser_side.split("+"):
        if element in positions:
            array[positions[element]] = -1

    return array

# Process each inequality according to the new rules
arrays_with_const = [create_array_from_inequality(ineq, positions_with_const) for ineq in inequalities]

# The initial arrays provided by the user
initial_arrays_with_const = [
    [0, -1, 0, -1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0]
]

# Combine the user-provided initial arrays with the newly processed ones
combined_arrays_with_const = initial_arrays_with_const + arrays_with_const
print(combined_arrays_with_const)
