from spleeter.separator import Separator

def separate(path: str):
    print('start separate')

    # setting spleeter separator
    separator = Separator('spleeter:5stems')

    # start separate
    separator.separate_to_file(path, 'result')

    print('end separate')