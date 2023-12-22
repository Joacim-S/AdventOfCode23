from data_reader import read_data

def get_hash(data):
    total = 0
    for row in data:
        if not row:
            break
        steps = row.split(',')
        for step in steps:
            total += hash_string(step)
    return total
        
def hash_string(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value = value % 256
    return value
    
if __name__ == '__main__':
    print(get_hash(read_data('15.txt')))