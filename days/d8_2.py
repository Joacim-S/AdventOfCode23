from data_reader import read_data

def count_total_steps(data):
    step_list = data[0].strip()
    node_map, nodes = get_map_and_starts(data[2:])
    steps = 0
    while True:
        for step in step_list:
            steps += 1
            done = True
            for i, node in enumerate(nodes):
                next_node = node_map[node][step]
                if next_node[-1] != 'Z':
                    done = False
                nodes[i] = next_node
            if done:
                return steps

def get_map_and_starts(data):
    starting_nodes = []
    node_map = {}
    for row in data:
        if not row:
            continue
        row = row.split('=')
        key = row[0].strip()
        if key[-1] == 'A':
            starting_nodes.append(key)
        values = row[1].split(', ')
        node_map[key] = {'L' : values[0][2:], 'R' : values[1][:-1]}
    return node_map, starting_nodes
if __name__ == '__main__':
    print(count_total_steps(read_data('8.txt')))