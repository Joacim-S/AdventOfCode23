from  data_reader import read_data

def get_margins(data):
    times = []
    distances = []
    row = data[0].split(' ')
    for value in row[1:]:
        if value:
            times.append(int(value.strip()))
    row = data[1].split(' ')
    for value in row[1:]:
        if value:
            distances.append(int(value.strip()))

    wins = []
    for time, distance in zip(times, distances):
        wins.append(get_ways_to_win(time, distance))
    
    total_ways = 1
    for win in wins:
        total_ways *= win

    return total_ways

def get_ways_to_win(time, distance):
    wins = 0
    for hold_time in range(time):
        if hold_time*(time-hold_time) > distance:
            wins += 1
    return wins

if __name__ == '__main__':
    print(get_margins(read_data('6.txt')))