from data_reader import read_data

def get_total_configurations(data):
    total = 0
    for row in data:
        if not row:
            break
        parts = row.split(' ')
        groups = parts[1].split(',')
        total += get_row_configurations(parts[0], groups)

def get_row_configurations(row, groups):
    streak = 0
    slots = []

    for char in row:
        pass



if __name__ == '__main__':
    print(get_total_configurations(read_data('12.txt')))