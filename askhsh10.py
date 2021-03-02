# importing the module
import ast


def dict_depth(dic):
    str_dic = str(dic)
    y = 0
    max = 0
    for i in str_dic:
        if i == "{" or i == "[":
            y += 1
            if max < y:
               max = y
        if i == "}" or i == "]":
            y -= 1
    return max


# reading the data from the file
with open('dic.txt') as f:
    data = f.read()

print("Data type before reconstruction : ", type(data))

# reconstructing the data as a dictionary
d = ast.literal_eval(data)

print("Data type after reconstruction : ", type(d))
print(d)
print(dict_depth(d))
