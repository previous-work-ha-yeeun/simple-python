
COVERAGE = 40
length_metres = float(input("Enter the length of the room in metres: "))
width_metres = float(input("Enter the width of the room in metres: "))
height_metres = float(input("Enter the height of the room in metres: "))
coats = int(input("Enter the number of coats: "))

surface_area = length_metres * width_metres + (length_metres + width_metres) * height_metres * 2
coverage_needed = surface_area * coats 
cans_of_paint_required = coverage_needed / COVERAGE
print(f"The number of cans of paint you need: {cans_of_paint_required}")


floor_value = int(cans_of_paint_required)
cans_to_buy = floor_value + (cans_of_paint_required - floor_value >0 )
print(f"Total number of cans to buy: {cans_to_buy}")


# import math
# cans_to_buy = math.ceil(cans_of_paint_required)