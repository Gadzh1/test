synonyms = {}

number = int(input())

for _ in range(number):
    words = input().split()
    syn_1 = words[0]
    syn_2 = words[1]

    synonyms[syn_1] = syn_2
    synonyms[syn_2] = syn_1

word = input()

print(synonyms.get(word, False))
