a = 'int'
b = 7
c = False
d = "18.5"

data_list = [a, b, c, d]

def checkType(data_list):
    for item in data_list:
        type(item)

print(checkType(data_list))
