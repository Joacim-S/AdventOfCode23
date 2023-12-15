from data_reader import read_data

def get_winnings(data):
    hands = []
    for row in data:
        if not row:
            continue
        hand = {}
        row = row.split(' ')
        hand['cards'] = row[0].strip()
        hand['bid'] = int(row[1].strip())
        hand['type'] = get_type(hand['cards'])
        print(hand['cards'], hand['type'])

def get_type(cards):
    kinds = {}
    for card in cards:
        if card not in kinds:
            kinds[card] = 1
        else:
            kinds[card] += 1

    if len(kinds) == 5:
        return 1
    
    if len(kinds) == 4:
        return 2
    
    if len(kinds) == 3:
        for count in kinds.values():
            if count == 3:
                return 4
        return 3
    
    if len(kinds) == 2:
        for count in kinds.values():
            if count == 3:
                return 5
        return 6
    
    return 7

def sort_by_cards(hand1, hand2):
    pass

print(get_winnings(read_data('7.txt')))