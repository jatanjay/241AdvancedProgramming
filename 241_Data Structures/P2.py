def areaCalc(radius):
	return 3.14 * radius * radius


def main():
	rad = float(input("enter the radius length: "))
	cir = areaCalc(rad)
	print(f"the area of the circle: {cir:.4f}")


if __name__ == '__main__':
	main()
