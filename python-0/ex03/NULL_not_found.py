import math

def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing: {object} {type(object)}")
	elif object == 0 and type(object) is int:
		print(f"Zero: {object} {type(object)}")
	elif type(object) is float:
		print(f"Cheese: {object} {type(object)}")
	elif object == '':
		print(f"Empty: {type(object)}")
	elif type(object) is bool:
		print(f"Fake: {object} {type(object)}")
	else:
		print("Type not Found")
		return 1
	return 0
	




# Nothing: None <class 'NoneType'>$			| NULL_not_found(Nothing)
# Cheese: nan <class 'float'>$				| NULL_not_found(Garlic)
# Zero: 0 <class 'int'>$					| NULL_not_found(Zero)
# Empty: <class 'str'>$						| NULL_not_found(Empty)
# Fake: False <class 'bool'>$				| NULL_not_found(Fake)
# Type not Found$							| print(NULL_not_found("Brian"))
# 1$


# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False
