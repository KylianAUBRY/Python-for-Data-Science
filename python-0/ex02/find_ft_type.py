
def all_thing_is_obj(object: any) -> int:

	type_name = {
		list: 	"List",
		tuple: 	"Tuple",
		set: 	"Set",
		dict: 	"Dict",
		str: 	f"{object} is in the kitchen",
	}

	if (type(object) in type_name):
		print(f"{type_name.get(type(object), 'Type not found')} : {type(object)}")
	else:
		print("Type not found")
	return 42


#python tester.py | cat -e
#List : <class 'list'>$
#Tuple : <class 'tuple'>$
#Set : <class 'set'>$
#Dict : <class 'dict'>$
#Brian is in the kitchen : <class 'str'>$
#Toto is in the kitchen : <class 'str'>$
#Type not found$
#42$