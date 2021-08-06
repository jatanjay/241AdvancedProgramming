# Jatan Pandya
# ECE - 241
# HW - 2 : P1.py
# Program to calculate Area and Circumference of a given circle

import math  # import math module for calculations


def calc_area(r):
	"""
	Calculates the area of the circle with formula pi * r^2
	:param r: radius of the circle
	:type r: float
	:return: area of the circle
	:rtype: float
	"""
	return math.pi * math.pow(r, 2)


def calc_cir(r):
	"""
	Calculates circumference of the circle with formula 2 * pi * r
	:param r: radius of the circle
	:type r: float
	:return: circumference of the circle
	:rtype: float
	"""
	return 2 * math.pi * r


if __name__ == '__main__':
	radius = float(input("\n Please enter the radius of the circle: "))  # ask user for radius of the circle
	print(f"\nThe radius of the circle is {radius:.4f} units")  # Display radius for the user
	print(
		f"\nThe area is {calc_area(radius):.4f} sq.units while the circumference is "
		f"{calc_cir(radius):.4f} units for a circle with radius {radius} units. "
		)
