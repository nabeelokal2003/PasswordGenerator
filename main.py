import random, string

def generatePassword():
    upp_1 = chr(random.randint(ord('A'), ord('Z')))
    upp_2 = chr(random.randint(ord('A'), ord('Z')))
    
    low_1 = chr(random.randint(ord('a'), ord('z')))
    low_2 = chr(random.randint(ord('a'), ord('z')))

    dig_1 = random.choice(string.digits)
    dig_2 = random.choice(string.digits)
    
    p_1 = random.choice(string.punctuation)
    p_2 = random.choice(string.punctuation)
    
    characters = [upp_1,upp_2,dig_1,dig_2,p_1,p_2,low_1,low_2]
    
    random.shuffle(characters)
    return characters

def duplicates(numOfDup):
    i = 0
    while i < numOfDup:
        result = ''.join(generatePassword()) 
        print("Password: ",''.join(result))
        i += 1
if __name__ == '__main__':
    duplicates(3)