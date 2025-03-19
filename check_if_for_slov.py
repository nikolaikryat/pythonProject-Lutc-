D = {'a': 1, 'b': 2, 'c': 3}
if not 'f' in D:
    print('missing')
    print('no, really..')

for key in D:
    print(key, '=>', D[key])