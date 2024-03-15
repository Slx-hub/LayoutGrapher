import re

def evaluate(data, keymap):
    prepared_data = filter_irrelevant_symbols(data, keymap)
    return get_all_bigrams(prepared_data, keymap)
    

def filter_irrelevant_symbols(data, keymap):
    known_keys = ''.join(keymap['left'].keys() | keymap['right'].keys())
    return re.sub('[^'+ known_keys + ']', ' ', data.lower())


def get_all_bigrams(data, keymap):
    bigrams = dict()
    for i in range(1, len(data)):
        if data[i] == ' ' or data[i-1] == ' ' or data[i] == data[i-1]:
            continue
        if (data[i] in keymap['left']) != (data[i-1] in keymap['left']):
            continue
        bigram = (data[i-1], data[i])
        if not bigram in bigrams:
            bigrams[bigram] = 0
        bigrams[bigram] += 1
    return bigrams