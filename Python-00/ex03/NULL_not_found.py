def NULL_not_found(object: any) -> int:
	var = {"NoneType":"Nothing",
		"float":"Cheese",
		"int":"Zero",
		"str":"Empty",
		"bool":"Fake"}

	if type(object) == str and len(object) != 0:
		print("Type not Found")
		return 1
	elif var[type(object).__name__]:
		print(var[type(object).__name__] + ":", object, type(object))
		return 0
	else:
		print("Type not Found")
		return 1

