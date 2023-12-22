from data_reader import read_data

def calculaate(data):
    gears = {}
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
            gear = (find_gear(data, row_i, start, i-1))
            if gear:
                if gear not in gears:
                    gears[gear] = []
                gears[gear].append(int(''.join(number)))
    
    result = 0
    for gear in gears.keys():
        if len(gears[gear]) == 2:
            result += gears[gear][0] * gears[gear][1]
    return result
            
def find_gear(data, row, start, end):
    try:
        if data[row][start-1] == '*' and start != 0:
            return (row, start-1)
    except:
        pass
    try:
        if data[row][end+1] == '*':
            return (row, end+1)
    except:
        pass
    for i in range(start, end+1):
        try:
            if data[row+1][i] == '*':
                return (row+1, i)
        except:
            pass
        try:
            if data[row-1][i] == '*' and row != 0:
                return (row+-1, i)
        except:
            pass
        try:
            if data[row+1][i-1] == '*' and i != 0:
                return (row+1, i-1)
        except:
            pass
        try:
            if data[row+1][i+1] == '*':
                return (row+1, i+1)
        except:
            pass
        try:
            if data[row-1][i-1] == '*' and row != 0 and i != 0:
                return (row-1, i-1)
        except:
            pass
        try:
            if data[row-1][i+1] == '*' and row != 0:
                return (row-1, i+1)
        except:
            pass
    return False


def find_next_number(row, i):
    while i < len(row) and not row[i].isdigit():
        i += 1
    return i

if __name__ == '__main__':
    print(calculaate(read_data('3.txt')))