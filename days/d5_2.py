from data_reader import read_data

def closest_location(data):
    seed_numbers = list(filter(lambda number: number, data[0].split(':')[1].split(' ')))
    maps = create_maps(data)
    distance = 10000000000000
    for i in range(0, len(seed_numbers), 2):
        seed = int(seed_numbers[i])
        seed_limit = int(seed_numbers[i]) + int(seed_numbers[i+1])
        while seed <= seed_limit:
            values = get_disgance((int(seed), int(seed_limit)), maps, 0)
            if values[0] < distance:
                distance = values[0]
            seed += (values[1] - values[0] + 1)
    return distance

def create_maps(data):
    maps = []
    current_map = -1
    for row in data[1:]:
        if not row:
            continue
        elif not row[0].isdigit():
            maps.append([])
            current_map += 1
        else:
            maps[current_map].append(row.split(' '))
    return maps

def get_disgance(value_range, maps, map_number):
    for row in maps[map_number]:
        if int(row[1]) <= value_range[0] <= (int(row[1]) + int(row[2])):
            new_value = int(row[0]) + (value_range[0] - int(row[1]))
            new_value_rannge = new_value, min((int(row[0]) + int(row[2])), (value_range[1] - value_range[0]) + new_value)
            if map_number == len(maps)-1:
                return new_value_rannge
            return get_disgance(new_value_rannge, maps, map_number+1)
    big_number = 1000000000000000000000000
    distance_to_closest = big_number
    for row in maps[map_number]:
        difference = int(row[1]) - value_range[0]
        if 0 < difference < distance_to_closest:
            distance_to_closest = difference

    return (big_number, big_number + distance_to_closest-1)

if __name__ == '__main__':
    print(closest_location(read_data('5.txt')))
