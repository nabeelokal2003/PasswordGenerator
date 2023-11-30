import random, string

length = -1
while length < 0:
    length = int(input('Enter the length of the password: '))


def get_characters():
    characters = string.ascii_letters + string.digits + string.punctuation
    character_set = []
    for i in characters:
         if len(character_set) != length:
             character_set.append(random.choice(characters))
    return character_set


print("You Password is ", ' '.join(get_characters()))