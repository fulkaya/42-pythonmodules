import sys


def main() -> None:
	print("=== Inventory System Analysis ===")

	inventory = {}

	for i in range(1, len(sys.argv)):
		param = sys.argv[i]
	
	if ":" not in param: 
		print(f"Error - invalid parameter '{param}'")
		continue

	parts = param.split(":")
	item = parts[0].strip()
	quantity_str = parts[1].strip()

	if item in inventory:
		print(f"Redundant item '{item}' - discarding")
		continue

	try:
		quantity = int(quantity_str)
		inventor[item] = quantity
	except ValueError as e:
		print(f"Quantity error for '{item}': {e}")
	
	if len(inventory) == 0:
		return
	
	print(f"Got inventory: {inventory}")

	
