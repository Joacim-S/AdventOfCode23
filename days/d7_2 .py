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
        hands.append(hand)
    hands.sort(key=sort_by_cards)
    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i+1)*hand['bid']
        
    return winnings

def get_type(cards):
    kinds = {}
    jokers = 0
    for card in cards:
        if card == 'J':
            jokers += 1
        elif card not in kinds:
            kinds[card] = 1
        else:
            kinds[card] += 1

    if len(kinds) == 5:
        return 1
    
    if len(kinds) == 4:
        return 2
    
    if len(kinds) == 3:
        for count in kinds.values():
            if count + jokers == 3:
                return 4
        return 3
    
    if len(kinds) == 2:
        for count in kinds.values():
            if count + jokers == 4:
                return 6
        return 5
    
    return 7

def sort_by_cards(hand):
    values = [hand['type']]
    for card in hand['cards']:
        if card == 'A':
            values.append(14)
        elif card == 'K':
            values.append(13)
        elif card == 'Q':
            values.append(12)
        elif card == 'J':
            values.append(1)
        elif card == 'T':
            values.append(10)
        else:
            values.append(int(card))
    return values

print(get_winnings(read_data('7.txt')))