file = open("C:\Documents\Advent-of-Code-2023\Day 4\inputs.txt", 'r')
input = file.read()
input_list = input.split('\n')



#Part 1
sum_1 = 0

for i in input_list:

    game = i.split(':')
    two_lst = game[1].split(' | ')
    three_lst = two_lst[0].split(' ')
    four_lst = two_lst[1].split(' ')
    matching = 0

    for j in four_lst:
        if j == "":
            continue
        if j in three_lst:
            matching += 1

    if matching == 0:
        continue
    else:
        sum_1 += 2 ** (matching - 1)
print(sum_1)

"""continue
print(j)
if j in three_lst:
    sum_1 += 1"""

