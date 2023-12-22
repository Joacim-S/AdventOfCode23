from data_reader import read_data

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

    furthest =  max(queue, key= lambda node: node[2])
    return furthest[2]
        
def get_connections(data, node):
    connections = []
    top_connections = '|7F'
    bottom_connections = '|LJ'
    left_connections = '-LF'
    right_connections = '-J7'

    try:
        if data[node[0]+1][node[1]] in bottom_connections:
            connections.append((node[0]+1, node[1], node[2]+1))
    except:
        pass

    try:
        if data[node[0]-1][node[1]] in top_connections:
            connections.append((node[0]-1, node[1], node[2]+1))
    except:
        pass

    try:
        if data[node[0]][node[1]-1] in left_connections:
            connections.append((node[0], node[1]-1, node[2]+1))
    except:
        pass

    try:
        if data[node[0]][node[1]+1] in right_connections:
            connections.append((node[0], node[1]+1, node[2]+1))
    except:
        pass

    return connections
    

def get_start(data):
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == 'S':
                return (y, x, 0)
            
print(get_max_distance(read_data('10.txt')))