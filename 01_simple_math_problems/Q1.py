PI = 3.14159

user_input = input("Enter a radius value for a sphere: ") 
radius = float(user_input)  # since input() returns a string

surface_area = 4 * PI * radius**2  # the radius squared
print("The surface area is:", surface_area)

volume = 4/3 * PI * radius**3  #  the radius cubed
print(f"The volume is: {volume:.2f}")  # formatted string 


double_radius = radius * 2
double_surface_area = 4 * PI * double_radius**2
double_volume = 4/3 * PI * double_radius**3

area_ratio = double_surface_area / surface_area
volume_ratio = double_volume / volume

print("When you double the radius, the surface area gets:", area_ratio, "times larger")
print(f"When you double the radius, the volume gets: {volume_ratio:.2f} times bigger")
# :.2f  →  fixed-point format, rounded to two decimal places