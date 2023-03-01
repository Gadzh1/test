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
files = []
actions_for_files = []

w = 'W'
r = 'R'
x = 'X'

n = int(input('Введите количество файлов '))

for i in range(n):
    file = input('Введите название файла и что с ним можно сделать ')
    if len(file.split()) > 4:
        print('Слишком много значений')
        break
    files.append(File(file.split()[0], w in file, r in file, x in file))

m = int(input('Введите количество действий '))

for _ in range(m):
    a = input('Введите действие и над каким файлом оно воспроизводится ')
    for f in files:
        if a.split()[1] == f.name:
            actions.append((a.split()[0], f))

for i in get_actions_results(actions):
    print(i)
