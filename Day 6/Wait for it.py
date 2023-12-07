def calculate_ways_to_win(race):
    ways_to_win = 0
    for hold_time in range(race["duration"]):
        speed = hold_time
        travel_time = race["duration"] - hold_time
        distance = speed * travel_time
        if distance > race["record_distance"]:
            ways_to_win += 1
    return ways_to_win

def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        raw_contents = file.read()

    time_line, distance_line = raw_contents.split('\n')
    times = list(map(int, time_line.split()[1:])) 
    distances = list(map(int, distance_line.split()[1:]))

    return [{"duration": t, "record_distance": d} for t, d in zip(times, distances)]

def calculate_total_ways_to_win(race_data):
    ways_to_win_each_race = [calculate_ways_to_win(race) for race in race_data]

    total_ways_to_win = 1
    for ways in ways_to_win_each_race:
        total_ways_to_win *= ways

    return total_ways_to_win, ways_to_win_each_race


file_path = 'C:/Documents/Advent-of-Code-2023/Day 6/inputs.txt'

race_data = read_and_parse_file(file_path)
total_ways_to_win, ways_to_win_each_race = calculate_total_ways_to_win(race_data)
print(total_ways_to_win, ways_to_win_each_race)