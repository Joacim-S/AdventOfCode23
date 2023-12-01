def read_data(file):
    with open(file) as input:
        data = input.read()
        return data
    
def get_numbers(row):
    written_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    current_string = ''
    digit1 = '0'
    digit2 = '0'
    for char in row:
        if char.isdigit():
            digit1 = char
            current_string = ''
            break
        current_string += char
        if current_string in written_digits:
            digit1 = written_digits[current_string]
            current_string = ''
            break

    for char in reversed(row):
        if char.isdigit():
            digit2 = char
            current_string = ''
            break
        current_string = char + current_string
        if current_string in written_digits:
            digit2 = written_digits[current_string]
            current_string = ''
            break
    return f'{digit1}{digit2}'

def get_sum(data):
    data = data.split('\n')
    sum = 0
    for row in data:
        print(int(get_numbers(row)))
        sum += int(get_numbers(row))
    return sum

if __name__ == '__main__':
    print(get_sum(read_data('calibration.txt')))