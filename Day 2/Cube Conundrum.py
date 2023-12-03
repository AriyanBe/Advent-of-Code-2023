file = open("C:\Documents\Advent-of-Code-2023\Day 2\inputs.txt", 'r')
input = file.read()
input_list = input.split('\n')

#Part 1
list_of_impossibles = ['12 red', '13 green', '14 blue']
sum1 = 0
for i in input_list:
    game = i.split(':')
    game_id = game[0].split('Game ')[1]
    valid = True
    cube = game[1].split(',')
    for j in cube:
        cube_attribute = j.split(';')
        for k in cube_attribute:
            numb = k.split(' ')
            if numb[2] == 'red':
                if int(numb[1]) > 12:
                    valid = False
            elif numb[2] == 'green':
                if int(numb[1]) > 13:
                    valid = False
            elif numb[2] == 'blue':
                if int(numb[1]) > 14:
                    valid = False
    if valid == True:
        sum1 += int(game_id)

print(sum1)


#Part 2
sum2 = 0
for i in input_list:
    game = i.split(':')
    game_id = game[0].split('Game ')[1]
    max_green = 0
    max_red = 0
    max_blue = 0
    cube = game[1].split(',')
    for j in cube:
        cube_attribute = j.split(';')
        for k in cube_attribute:
            numb = k.split(' ')
            if numb[2] == 'red':
                if int(numb[1]) > max_red:
                    max_red = int(numb[1])

            elif numb[2] == 'green':
                if int(numb[1]) > max_green:
                    max_green = int(numb[1])

            elif numb[2] == 'blue':
                if int(numb[1]) > max_blue:
                    max_blue = int(numb[1])

    max_multiplied = max_green * max_red * max_blue
    sum2 += max_multiplied
print(sum2)