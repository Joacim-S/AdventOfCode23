from data_reader import read_data

def closest_location(data):
    seeds = {}
    seed_numbers = list(filter(lambda number: number, data[0].split(':')[1].split(' ')))
    maps = create_maps(data)
    distances = []
    for seed in seed_numbers:
        distances.append(get_disgance(int(seed), maps, 0))
    return min(distances)

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

def get_disgance(value, maps, map_number):
    for row in maps[map_number]:
        if int(row[1]) <= value <= int(row[1]) + int(row[2]):
            new_value = int(row[0]) + (value - int(row[1]))
            if map_number == len(maps)-1:
                return new_value
            return get_disgance(new_value, maps, map_number+1)
    return 1000000000000000

if __name__ == '__main__':
    print(closest_location(read_data('5.txt')))