from data_reader import read_data

def get_load(data):
    total = 0
    loads = {}
    for y, row in enumerate(data):
        if not row:
            continue
        for x, spot in enumerate(row):
            if spot == '.':
                continue
            weight = len(data) - y

            if x not in loads:
                loads[x] = set()
                if spot == 'O':
                    loads[x].add(len(data))
                    total += len(data)
                if spot == '#':
                    loads[x].add(weight)
                continue

            if spot == 'O':
                weight = min(filter(lambda load : load > 0, loads[x])) - 1
                total += weight
                loads[x].add(weight)
            elif spot == '#':
                loads[x].add(weight)

    return total

if __name__ == '__main__':
    print(get_load(read_data('14.txt')))
