import time

"""
Temperature Conversion:
Returns temperature in celsius if in fahrenheit or vice versa.

Parameters:
temp(float) = Temperature (in C or F) as a floating point number
mode(int) = 0 if you want to convert F -> C, 1 if you want to convert C -> F
"""
def temp_conversion(temp: float, mode: int) -> float:
	frac = 9 / 5
	const = 32
	return round(temp * frac + const if mode else ((temp - const) / frac), 2)

"""
Stacked Bag Formula:
Returns the estimated warmth rating of two sleeping bags used together.

Note: Order doesn't matter, the function will change the formula according to the relative temperatures. However,
it is recommended that you put the colder sleeping bag in the warmer one as space permits.

Parameters:
bag_1(float) = Temperature (F) rating of the first bag.
bag_2(float) = Temperature (F) rating of the second bag.
"""
def stacked_bag_warmth(bag_1: float, bag_2: float) -> float:
	if bag_1 >= bag_2:
		return bag_2 - ((70 - bag_1) / 2)
	return bag_1 - ((70 - bag_2) / 2)

"""
2+ Stacked Bag Calculator:
Returns the estimated warmth rating of 2 or more sleeping bags used together. Returns 9999 if input is invalid.

Note: Warmth may vary depending on how the sleeping bags are layered. At this point it may be better to just purchase
a warmer sleeping bag.

Parameters:
bags(tuple of floats): Temperature ratings of all bags used simultaneously.
"""
def three_plus_bags_warmth(*bags: float) -> float:
	if len(bags) == 2:
		return stacked_bag_warmth(bags[0], bags[1])
	elif len(bags) > 2:
		return stacked_bag_warmth(bags[0], three_plus_bags_warmth(*bags[1:]))
	elif len(bags) == 1:
		return bags[0]
	return 9999

"""
2+ Bags Celsius:
Returns the estimated warmth rating of 2 or more sleeping bags used together. Takes and returns temps in celsius

Parameters:
bags(tuple of floats): Temperature ratings of all bags used simultaneously.
"""
def celsius_bags(*bags: float) -> float:
	x = lambda a: temp_conversion(a, 1)
	return temp_conversion(three_plus_bags_warmth(*tuple(map(x, bags))), 0)

"""
Prompts for sleeping bag temperatures and applies the appropriate functions/calculations.
"""

def calculation_prompt() -> None:

	# Loops while user wants to keep making calculations
	while True:
		# Determines the proper calculation functions based on desired units
		unit = ''
		calc_func = {'C': celsius_bags, 'F': three_plus_bags_warmth}
		while True:
			res = input("Please enter the desired temperature unit (C/F): ").upper()
			if res == 'C' or res  == 'F':
				unit = res
				break
		print("\n")

		temps = []
		i = 1

		# Allows user to add temperature ratings line by line
		print("~~~ Please enter the temperature of each sleeping bag in {}° ~~~".format(unit))
		while True:
			temp = input("\nSleeping bag {}: ".format(i))
			if not temp:
				break
			temps.append(float(temp))
			print("°{} ".format(unit).join(map(str, temps)) + "°{} ".format(unit))
			i += 1
		print("~~~ Estimated Temperature Rating: {}°{} ~~~".format(calc_func[unit](*tuple(temps)), unit))
		
		# Loops until user gives a valid response, breaks all loops if n is inputted, only breaks internal prompt loop
		# if y is inputted
		while True:
			res = input("\nDo you want to make another calculation? (y/n)").upper()
			if res == 'Y':
				print("\n")
				break
			elif res == 'N':
				return

if __name__ == '__main__':
	calculation_prompt()