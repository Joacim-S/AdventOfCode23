from data_reader import read_data
#Does not work at all
def get_max_distance(data):
    start = get_start(data)
    i = 0
    visited = set()
    queue = [start]
    while i < len(queue):
        visited.add(queue[i][:2])
        connections = get_connections(data, queue[i])
        for c in connections:
            if c[:2] not in visited:
                queue.append(c)
        i += 1
    plots = list(filter(lambda node: node[2] == 0, queue))
    return len(plots)
        
def get_connections(data, node):
    connections = []

    try:
        if data[node[0]+1][node[1]] != '#' and node[2]+1 <= 65:
            connections.append((node[0]+1, node[1], node[2]+1))
    except:
        pass

    try:
        if data[node[0]-1][node[1]] != '#' and node[2]+1 <= 65:
            connections.append((node[0]-1, node[1], node[2]+1))
    except:
        pass

    try:
        if data[node[0]][node[1]-1] != '#' and node[2]+1 <= 65:
            connections.append((node[0], node[1]-1, node[2]+1))
    except:
        pass

    try:
        if data[node[0]][node[1]+1] != '#' and node[2]+1 <= 65:
            connections.append((node[0], node[1]+1, node[2]+1))
    except:
        pass

    return connections
    

def get_start(data):
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == 'S':
                return (y, x, 0)
            
print(get_max_distance(read_data('21.txt')))