def calc_pizza_volume(pizza_diameter, pizza_height):
   pi_val = 3.14159265

   pizza_radius = pizza_diameter / 2.0
   pizza_area = pi_val * pizza_radius * pizza_radius
   pizza_volume = pizza_area * pizza_height
   return pizza_volume

print(f'12.0 x 0.3 inch pizza is {calc_pizza_volume(12.0, 0.3):.3f} cubic inches.')

print(f'12.0 x 0.8 inch pizza is {calc_pizza_volume(12.0, 0.8):.3f} cubic inches.')

print(f'16.0 x 0.8 inch pizza is {calc_pizza_volume(16.0, 0.8):.3f} cubic inches.')