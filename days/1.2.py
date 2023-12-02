from data_reader import read_data

def get_numbers(row):
    current_string = ''
    digit1 = '0'
    digit2 = '0'
    for char in row:
        if char.isdigit():
            digit1 = char
            current_string = ''
            break
        current_string += char
        result = check_string(current_string)
        if result:
            current_string = ''
            digit1 = result
            break

    for char in reversed(row):
        if char.isdigit():
            digit2 = char
            current_string = ''
            break
        current_string = char + current_string
        result = check_string(current_string)
        if result:
            current_string = ''
            digit2 = result
            break


    return f'{digit1}{digit2}'

def check_string(string):
    written_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for digit in written_digits.keys():
        if digit in string:
            return written_digits[digit]


def get_sum(data):
    sum = 0
    for row in data:
        sum += int(get_numbers(row))
    return sum

if __name__ == '__main__':
    print(get_sum(read_data('1.txt')))