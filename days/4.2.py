from data_reader import read_data

def calculate(data):
    for row in data:
        if not row:
            break
        row = row.split(':')
        game = int(row[0][5:])
        print(game)
        numbers = row[1].split('|')
        winners = set(filter(lambda number: number, numbers[0].split(' ')))
        print(winners)

if __name__ == '__main__':
    print(calculate(read_data('4.txt')))