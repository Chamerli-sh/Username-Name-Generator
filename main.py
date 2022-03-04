import random
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'y', 'v' 'w', 'x', 'y', 'z']
voyels = ['a', 'i', 'u' 'e', 'o', 'oo', 'io', 'oy', 'ai', 'ui']

types = [consonants, voyels]

random.shuffle(consonants)
username = ""
usr_len = int(input("Enter the lenght of your usename: "))
i = 0
random.shuffle(types)
while i <= usr_len:
    random.shuffle(consonants)
    username += types[0][0]

    random.shuffle(voyels)
    username += types[1][0]
    i += 1

print(username)