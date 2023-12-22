from data_reader import read_data

def extrapolate(data):
    total = 0
    for row in data:
        if not row:
            continue
        numbers = [int(x) for x in row.split(' ')]
        total += predict(numbers)
    return total

def predict(numbers):
    last_numbers = []
    current_row = numbers
    last_row = False

    while not last_row:
        last_row = True
        last_numbers.append(current_row[-1])
        next_row = []

        for i in range(1, len(current_row)):
            next_value = (current_row[i] - current_row[i-1])
            if next_value:
                last_row = False
            next_row.append(next_value)

        current_row = next_row

    return sum(last_numbers)

if __name__ == '__main__':
    print(extrapolate(read_data('9.txt')))