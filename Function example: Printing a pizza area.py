def calc_pizza_area():
 pi_val = 3.14159265

 pizza_diameter = 12.0
 pizza_radius = pizza_diameter / 2.0
 pizza_area = pi_val * pizza_radius * pizza_radius
 return pizza_area

print(f'{12:.1f} inch pizza is {calc_pizza_area():.3f} square inches')