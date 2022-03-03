import random
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'y', 'v' 'w', 'x', 'y', 'z']
voyels = ['a', 'i', 'u' 'e', 'o', 'o', 'io']

types = [consonants, voyels]

random.shuffle(consonants)

usr_len = 5
i = 0
random.shuffle(types)
while i <= usr_len:
    random.shuffle(consonants)
    print(types[0][0])
    random.shuffle(voyels)
    print(types[1][0])
    i += 1