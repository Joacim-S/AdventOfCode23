def read_data(file):
    with open(f'inputs/{file}') as input:
        data = input.read().split('\n')
        return data