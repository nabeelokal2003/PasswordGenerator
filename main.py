import random, string

# length = -1
# while length < 0:
#     length = int(input('Enter the length of the password: '))



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
        print("You Password is ", ''.join(get_characters()))
        print('\n')
        i += 1

def check_letters(text):
    words = text.split()
    answer = ''
    count_upper = 0
    count_lower = 0
    count_digit = 0
    for i in text:
        if words[i].isupper():
            count_upper += 1
            answer += words[i]
        if count_upper == 2:
            if words[i].lower():
                count_lower += 1
                answer += words[i]
            if count_lower == 2:
                if words[i].isdigit():
                   count_digit += 1
                   answer += words[i]
                if count_digit == 2:
                    return True
                i += 1
            i += 1
        i += 1
print(check_letters('aN4'))