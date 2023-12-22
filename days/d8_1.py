from data_reader import read_data

def count_steps(data):
    step_list = data[0].strip()
    node_map = get_map(data[2:])
    current_node = 'AAA'
    steps = 0
    while current_node != 'ZZZ':
        for step in step_list:
            steps += 1
            node = node_map[current_node][step]
            current_node = node
    return steps

def get_map(data):
    node_map = {}
    for row in data:
        if not row:
            continue
        row = row.split('=')
        key = row[0].strip()
        values = row[1].split(', ')
        node_map[key] = {'L' : values[0][2:], 'R' : values[1][:-1]}
    return node_map
if __name__ == '__main__':
    print(count_steps(read_data('8.txt')))