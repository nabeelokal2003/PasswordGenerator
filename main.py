import random, string

def get_characters():
    characters = string.ascii_letters + string.digits + string.punctuation
    character_set = []
    for i in characters:
         if len(character_set) != 8:
             character_set.append(random.choice(characters))
    return character_set

def duplicates(numOfDup):
    i = 0
    while i < numOfDup:
        print("You Password is ", ''.join(password_restriction()))
        print('\n')
        i += 1
def password_restriction():
    text = get_characters()
    result = ''
    countUpper = countLower = countDigit = countPunc = 0
    for i in range(len(text)):
        if text[i].isupper() and countUpper < 2:
            countUpper += 1
            result += text[i]
        elif text[i].islower() and countLower < 2:
            countLower += 1
            result += text[i]
        elif text[i].isdigit() and countDigit < 2:
            countDigit += 1
            result += text[i]
        elif text[i] in string.punctuation and countPunc < 2:
            countPunc += 1
            result += text[i]
    return result

if __name__ == '__main__':
    duplicates(3)