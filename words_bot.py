import random
from copy import deepcopy
from collections import defaultdict

#invalid chars
inv_chrs = 'ьъы'

# returns last valid char from input string
def get_last_chr(inputstr):
    i = 1
    while inputstr[-i] in inv_chrs and i < len(inputstr):
        i = i + 1
    last_chr = inputstr[-i]
    if last_chr in inv_chrs:
        last_chr = None
    return last_chr


# returns first char for non-empty string
def get_first_chr(inputstr):
    if len(inputstr) != 0:
        first_chr = inputstr[0]
    else:
        first_chr = ""
    return first_chr


# importing txt file and making a dictionary
with open('wg.txt') as slova:
    words = defaultdict(list)
    lines = [line.strip() for line in slova]
    for word in lines:
        words[word[0]].append(word)


# try count
count = 0

# copy of a dictionary
words_copy = deepcopy(words)


# bot new turn
def bot_turn(player_word):
    first_char = get_first_chr(player_word)
    if player_word in words_copy[first_char]:
        del words_copy[first_char][words_copy[first_char].index(player_word)]

    first_bot_letter = get_last_chr(player_word)
    print("So, my first letter is: ", first_bot_letter)
    available_words_count = len(words_copy[first_bot_letter])
    if available_words_count == 0:
        return "Error"
    bot_choice_index = random.randrange(0, available_words_count)
    available_words = words_copy[first_bot_letter]
    bot_choice = available_words[bot_choice_index]

    del words_copy[first_bot_letter][bot_choice_index]
    print("My new word is: ", bot_choice)
    print("Your first letter is: ", get_last_chr(bot_choice))
    return get_last_chr(bot_choice)

first_turn = True

# player's turn
def player_turn(required_first_char):
    global first_turn
    while True:
        print("Print a word: ")
        player_word = str(input()).lower()
        if first_turn:
            required_first_char = get_first_chr(player_word)
        if ((player_word in words_copy[required_first_char]) or player_word == "stop"):
            break
        else:
            print("Invalid first char or already used word, try another word: ")
    first_turn = False
    return player_word


first_required_char = ""
print("Welcome here! To stop print \"stop\". Enjoy this game!\n")
while True:
    new_player_word = player_turn(first_required_char)
    count += 1
    if new_player_word != "stop":
        first_required_char = bot_turn(new_player_word)
        if first_required_char == "Error":
            print("You're winner! Your result is ", count, " words!")
            break
    else:
        print("You're looser! Your result is ", count, " words!")
        break