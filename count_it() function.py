def count_it(sequence):
    dictt = {int(item): sequence.count(item) for item in sequence}
    res = sorted(dictt.items(), key=lambda a: a[1])
    return dict(res[-3:])


print(count_it('123134311'))
