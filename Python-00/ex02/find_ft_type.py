def all_thing_is_obj(object: any) -> int:
	# print("----------> ", type(object).__name__)
	if type(object) == str:
		print(object , "is in the kitchen :", type(object))
	elif type(object) == int:
		print("Type not found")
	else:
		print(type(object).__name__, " : ", type(object))
	return 42
