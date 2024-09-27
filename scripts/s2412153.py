import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python ball_cml.py <v0> <t>")
    sys.exit(1)

# Read v0 and t from the command line
v0 = float(sys.argv[1])
t = float(sys.argv[2])

# Define the gravitational constant
g = 9.81

# Calculate the formula y(t) = v0*t - 0.5*g*t**2
y = v0 * t - 0.5 * g * t ** 2

# Print the result
print(f"The height y after {t} seconds is {y:.2f} meters.")
