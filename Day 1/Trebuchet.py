file = open("C:\Documents\Advent-of-Code-2023\Day 1\inputs.txt", 'r')
input = file.read()
input_list = input.split('\n')

# part 1
sum = 0 
for inp in input_list:
    nums = []
    for letter in inp:
        if ord(letter) <= 57:
            nums.append(letter) 

    sum += int(nums[0] + nums[-1])

# part 2
sum = 0 
integer_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for inp in input_list:
    nums = [] 
    for i, letter in enumerate(inp):
        for val, name in enumerate(integer_names):
            if name in inp[i:i+len(name)]:
                nums.append(str(val)) 
        if ord(letter) <= 57: 
            nums.append(letter)


    sum += int(nums[0] + nums[-1])

print(sum)