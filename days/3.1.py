from data_reader import read_data

def calculaate(data):
    total = 0
    for row_i, row in enumerate(data):
        i = 0
        while i < len(row):
            number = []
            i = find_next_number(row, i)
            start = i
            while i < len(row) and row[i].isdigit():
                number.append(row[i])
                i += 1
            if is_part_numer(data, row_i, start, i-1):
                total += int(''.join(number))
    return total
            
def is_part_numer(data, row, start, end):
    part_mumber = False
    try:
        if data[row][start-1] != '.' and start != 0:
            part_mumber = True
    except:
        pass
    try:
        if data[row][end+1] != '.':
            part_mumber = True
    except:
        pass
    for i in range(start, end+1):
        try:
            if data[row+1][i] != '.':
                part_mumber = True
        except:
            pass
        try:
            if data[row-1][i] != '.' and row != 0:
                part_mumber = True
        except:
            pass
        try:
            if data[row+1][i-1] != '.' and i != 0:
                part_mumber = True
        except:
            pass
        try:
            if data[row+1][i+1] != '.':
                part_mumber = True
        except:
            pass
        try:
            if data[row-1][i-1] != '.'and row != 0 and i != 0:
                part_mumber = True
        except:
            pass
        try:
            if data[row-1][i+1] != '.'and row != 0:
                part_mumber = True
        except:
            pass
    return part_mumber


def find_next_number(row, i):
    while i < len(row) and not row[i].isdigit():
        i += 1
    return i

if __name__ == '__main__':
    print(calculaate(read_data('3.txt')))