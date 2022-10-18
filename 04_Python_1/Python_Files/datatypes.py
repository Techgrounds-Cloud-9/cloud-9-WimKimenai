a = 'int'
b = 7
c = False
d = "18.5"

data_list = [a, b, c, d]

def checkType(data_list):
    for item in data_list:
        if isinstance(item, int):
            print(item, "= Integer")
        if isinstance(item, bool):
            print(item, "= Boolean")
        if isinstance(item, set):
            print(item, "= Set")
        if isinstance(item, str):
            print(item, "= String")
        if isinstance(item, float):
            print(item, "= Floating point number")
        if isinstance(item, list):
            print(item, "= List")
        if isinstance(item, tuple):
            print(item, "= Tuple")
        if isinstance(item, dict):
            print(item, "= Dictionary")
        if isinstance(item, complex):
            print(item, "= Complex")

print(checkType(data_list))
