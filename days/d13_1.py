from data_reader import read_data

def summarize(data):
    total = 0
    pictures = get_pictures(data)
    for picture in pictures:
        total += summarize_pic(picture)
    return total

def get_pictures(data):
    pictures = []
    picture = []
    for row in data:
        if not row:
            pictures.append(picture)
            picture = []
        else:
            picture.append(row)
    if picture:
        pictures.append(picture)
    return pictures

def summarize_pic(picture):
    row_value = get_value(picture, 100)
    if row_value:
        return row_value
    transformed = transform(picture)
    column_value = get_value(transformed, 1)

    return column_value

def transform(picture):
    columns = [[] for x in range(len(picture[0]))]
    for row in picture:
        for i, char in enumerate(row):
            columns[i].append(char)
    return columns

    


def get_value(picture, multiplier):
    for i in range(1, len(picture)):
        distance = 0
        match = True
        while i - distance > 0 and i + distance < len(picture):
            if not picture[i + distance] == picture[i - 1 - distance]:
                match = False
            distance += 1
        if match:
            return i * multiplier
    return 0

if __name__ == '__main__':
    print(summarize(read_data('13.txt')))