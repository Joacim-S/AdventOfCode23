

def read_data(file):
    with open(file) as input:
        data = input.read()
        return data
    
def get_numbers(row):
    digit1 = '0'
    digit2 = '0'
    for char in row:
        if char.isdigit():
            digit1 = char
            break
    for char in reversed(row):
        if char.isdigit():
            digit2 = char
            break
    return f'{digit1}{digit2}'

def get_sum(data):
    data = data.split('\n')
    sum = 0
    for row in data:
        sum += int(get_numbers(row))
    return sum

if __name__ == '__main__':
    print(get_sum(read_data('input.txt')))