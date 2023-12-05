from data_reader import read_data

def calculate(data):
    total = 0
    for row in data:
        winners_collected = False
        winners = set()
        my_numbers = []
        score = 0
        i = 0
        number = ''
        while i < len(row):
            if not i:
                while row[i] != ':':
                    i += 1

            elif row[i] == ' ' and number:
                if winners_collected:
                    my_numbers.append(int(number))
                else:
                    winners.add(int(number))
                number = ''

            elif row[i] == '|':
                winners_collected = True

            elif row[i].isdigit():
                number += row[i]


            i += 1

        if number:
            my_numbers.append(int(number))

        for number in my_numbers:
            if number in winners:
                if not score:
                    score = 1
                else:
                    score *= 2

        total += score

    return total
    

if __name__ == '__main__':
    print(calculate(read_data('4.txt')))