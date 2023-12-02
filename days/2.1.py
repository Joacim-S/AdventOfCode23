from data_reader import read_data

def calculaate(data):
    values = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    for row in data:
        ok = True
        row = row.split(':')
        game_id = int(row[0][5:])
        results = row[1].split(';')
        for result in results:
            items = result.split(',')
            for item in items:
                item = item.split(' ')
                if int(item[1]) > values[item[2]]:
                    ok = False
        if ok:
            sum += game_id
    return sum
        

if __name__ == '__main__':
    print(calculaate(read_data('2.txt')))