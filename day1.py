import re
with open("day1_input", 'r') as file:
    entries = file.readlines()

options=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
string_to_digit = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

numbers = []
first, second = str(), str()

for ent in entries:
    ent.replace('\n','')

    fw_dict = {}
    for o in options:
        if o in ent:
            fw_dict[ent.index(o)] = o
    indexes = (list(fw_dict.keys()))
    if len(indexes) != 0:
        smallest = min(indexes)
        biggest = max(indexes)
    else:
        smallest = len(ent)+1
        biggest = -1

    fw_ind = -1
    rv_ind = len(ent)

    for x in ent:
        fw_ind += 1
        if x.isdigit():
            first = x
            break
        if fw_ind >= smallest:
            first = string_to_digit[fw_dict[smallest]]
            break

    rev = ent[::-1]
    for y in rev:
        rv_ind -=1
        if y.isdigit():
            second = y
            break
        if rv_ind <= biggest:
            second = string_to_digit[fw_dict[biggest]]
            break

    valu = first+second
    numbers.append(int(valu))

print(sum(numbers))
