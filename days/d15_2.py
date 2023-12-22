from data_reader import read_data
from d15_1 import hash_string

def get_focusing_power(data):
    boxes = place_lenses(data)
    total_power = 0
    for i, box in boxes.items():
        for k, power in enumerate(box.values()):
            total_power += (1 + i) * (k + 1) * power
    
    return total_power


def place_lenses(data):
    boxes = {x : {} for x in range(256)}
    total = 0
    for row in data:
        if not row:
            break
        steps = row.split(',')
        for step in steps:
            label = ''
            for i, char in enumerate(step):
                if char.isalpha():
                    label += char
                else:
                    box = hash_string(label)
                    if char == '=':
                        boxes[box][label] = int(step[i+1:])
                    if char == '-':
                        if label in boxes[box]:
                            boxes[box].pop(label)
    return boxes

if __name__ == '__main__':
    print(get_focusing_power(read_data('15.txt')))