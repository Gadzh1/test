class File:
    def __init__(self, name, w=False, r=False, e=False):
        self.name = name
        self.w = w
        self.r = r
        self.e = e

    def is_writable(self):
        return self.w

    def is_readable(self):
        return self.r

    def is_executable(self):
        return self.e


def get_actions_results(listt: list):
    results = []
    for a, f in listt:
        if a == 'read' and f.is_readable():
            results.append('OK')
            continue
        if a == 'write' and f.is_writable():
            results.append('OK')
            continue
        if a == 'execute' and f.is_executable():
            results.append('OK')
            continue
        results.append('Access denied')
    return results


actions = []
n = int(input('Введите количество файлов '))
m = int(input('Введите количество действий '))


for n in range(n):
    for m in range(m):
        name = input('Введите название файла и что с ним можно делать ')
        w = 'W'
        r = 'R'
        x = 'X'
        action = input('Введите действие ')
        if len(name.split()) > 4:
            print('Слишком много значений')
            break
        if len(name.split()) == 4:
            actions.append((action, File(name.split()[0], True, True, True)))

        if len(name.split()) == 3:

            if w in name and r in name:
                actions.append((action, File(name.split()[0], True, True)))
            elif w in name and x in name:
                actions.append((action, File(name.split()[0], True, False, True)))
            elif r in name and x in name:
                actions.append((action, File(name.split()[0], False, True, True)))

        elif w in name:
            actions.append((action, File(name.split()[0], True)))
        elif r in name:
            actions.append((action, File(name.split()[0], False, True)))
        elif x in name:
            actions.append((action, File(name.split()[0], False, False, True)))
else:
    print('не указано что можно делать с файлом')


for i in get_actions_results(actions):
    print(i)
print(1)
