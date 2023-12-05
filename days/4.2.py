from data_reader import read_data

def calculate(data):
    games = {}
    for row in data:
        if not row:
            break
        row = row.split(':')
        game = int(row[0][5:])
        numbers = row[1].split('|')
        winners = get_numbers(numbers[0])
        my_numbers = get_numbers(numbers[1])
        wins = get_wins(my_numbers, winners)
        print(wins)
        
def get_wins(numbers, winners):
    wins = 0
    for n in numbers:
        if n in winners:
            wins += 1
    
    return wins

def get_numbers(number_string):
    numbers = set(filter(lambda number: number, number_string.split(' ')))
    return numbers

if __name__ == '__main__':
    print(calculate(read_data('4test.txt')))