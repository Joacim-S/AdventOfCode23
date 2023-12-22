from data_reader import read_data

def calculaate(data):
    powers = []
    for row in data:
        values = {'red': 0, 'green': 0, 'blue': 0}
        ok = True
        row = row.split(':')
        game_id = int(row[0][5:])
        results = row[1].split(';')
        for result in results:
            items = result.split(',')
            for item in items:
                item = item.split(' ')
                if int(item[1]) > values[item[2]]:
                    values[item[2]] = int(item[1])
        power = 1
        for number in values.values():
            power *= number
        powers.append(power)
    return sum(powers)

if __name__ == '__main__':
    print(calculaate(read_data('2.txt')))