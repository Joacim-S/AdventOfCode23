from data_reader import read_data

def get_distances(data, expansion_factor):
    total_distance = 0
    galaxies = get_galaxies(data, expansion_factor)
    for i, g in enumerate(galaxies):
        for other_g in galaxies[i+1:]:
            total_distance += abs(g[0] - other_g[0]) + abs(g[1] - other_g[1])
    
    return total_distance

def get_galaxies(data, expansion_factor):
    galaxies = []
    offset = 0
    for y, row in enumerate(data):
        empty_row = True
        for x, char in enumerate(row):
            if char == '#':
                empty_row = False
                galaxies.append([x, y + offset])
        if empty_row:
            offset += expansion_factor-1
    final_galaxies = add_cols(galaxies, expansion_factor)
    return final_galaxies
    

def add_cols(galaxies, expansion_factor):
    galaxies.sort()
    offset = 0
    galaxies_expanded = []
    for i, g in enumerate(galaxies):
        galaxies_expanded.append((g[0] + offset, g[1]))

        if i == len(galaxies)-1:
            return galaxies_expanded

        col_difference = galaxies[i+1][0] - g[0]
        if col_difference > 1:
            offset += (col_difference - 1) * (expansion_factor-1)



if __name__ == '__main__':
    print(get_distances(read_data('11.txt'), 1000000))