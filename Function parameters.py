import math
	
def calc_pizza_area(pizza_diameter):
   pizza_radius = pizza_diameter / 2.0
   pizza_area = math.pi * pizza_radius * pizza_radius
   return pizza_area
	
print(f'12.0 inch pizza is {calc_pizza_area(12.0):.3f} square inches')
print(f'16.0 inch pizza is {calc_pizza_area(16.0):.3f} square inches')