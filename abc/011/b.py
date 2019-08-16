string = raw_input()
new_string = ""

str_list = list(string)

for i,s in enumerate(str_list):
    if i == 0:
        new_string += s.upper()
    else:
        new_string += s.lower()

print new_string
