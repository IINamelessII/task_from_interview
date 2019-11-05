from pprint import pprint


DATA = {
    'categ1': [
        {
            'name': 'name1',
            'amount': 100,
            'sub': {
                'rate': 55,
                'hot': False
            }
        },
        {
            'name': 'name2',
            'amount': 200,
            'sub': {
                'rate': 99,
                'hot': True
            }
        }
    ],
    'categ2': {
        'atr1': 'simple',
        'atr2': 'Another'
    }
}


def convert(data): #WITH RECURSION
    def f(obj, s):
        if isinstance(obj, dict):
            for key, value in obj.items():
                f(value, f'{s}.{key}' if s else key)
        elif isinstance(obj, list):
            for i in range(len(obj)):
                f(obj[i], f'{s}.{i}' if s else key)
        else:
            a[s] = obj

    a = dict()
    f(data, '')
    return a


def conv(data): #WITHOUT RECURSION
    a, indexes = dict(), list()
    while (not len(indexes)) or len(data) > indexes[0]:
        obj, s, level = data, '', 0

        while True: #Going deeper
            if level == len(indexes) and (isinstance(obj, dict) or isinstance(obj, list)):
                indexes.append(0)
                index = 0
            elif isinstance(obj, dict) or isinstance(obj, list):
                index = indexes[level]

            if isinstance(obj, dict):
                if len(obj) == index:
                    indexes[level - 1] += 1
                    indexes[level:] = [0] * (len(indexes) - level)
                    break
                s += ('.' if s else '') + (list(obj.keys())[index])
                obj = list(obj.values())[index]
                level += 1

            elif isinstance(obj, list):
                if len(obj) == index:
                    indexes[level - 1] += 1
                    indexes[level:] = [0] * (len(indexes) - level)
                    break
                s += ('.' if s else '') + str(index)
                obj = obj[index]        
                level += 1

            else:
                indexes[level - 1] += 1
                indexes[level:] = [0] * (len(indexes) - level)
                a[s] = obj
                break

    return a

print('WITH RECURSION:')
pprint(convert(DATA))
print('\nWITHOUT RECURSION:')
pprint(conv(DATA))
