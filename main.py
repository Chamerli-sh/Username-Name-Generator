import random
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'y', 'v' 'w', 'x', 'y', 'z']
voyels = ['a', 'i', 'u' 'e', 'o']

random.shuffle(consonants)

usr_len = 5
i = 0
while i <= usr_len:
    random.shuffle(consonants)
    print(consonants[0])
    random.shuffle(voyels)
    print(voyels[0])
    i += 1