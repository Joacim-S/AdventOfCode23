from multiprocessing import Process
from data_reader import read_data

def slow_closest_location(data):
    seed_numbers = list(filter(lambda number: number, data[0].split(':')[1].split(' ')))
    maps = create_maps(data)
    distance = 10000000000000
    processes = []
    for i in range(0, len(seed_numbers), 2):
        print(i)
        seed = int(seed_numbers[i])
        seed_limit = int(seed_numbers[i]) + int(seed_numbers[i+1])
        p = Process(target=get_disgance_in_range, args=(seed, seed_limit, maps, 0))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

def get_disgance_in_range(seed, seed_limit, maps, map_number):
    distance = 10000000000000
    while seed <= seed_limit:
        value = get_disgance_old(int(seed), maps, 0)
        if value < distance:
            distance = value
        seed += 1
    print(distance)

def get_disgance_old(value, maps, map_number):
    for row in maps[map_number]:
        if int(row[1]) <= value <= int(row[1]) + int(row[2]):
            new_value = int(row[0]) + (value - int(row[1]))
            if map_number == len(maps)-1:
                return new_value
            return get_disgance_old(new_value, maps, map_number+1)
    return 1000000000000000

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

if __name__ == '__main__':
    slow_closest_location(read_data('5.txt'))