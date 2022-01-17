# How many letters deep should we go?
depth = 9
# Get the words
import requests
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
response = requests.get(url)

# Parse the words into a list
response.encoding = response.apparent_encoding
words = response.text.split('\n')

# Filter the words
import re
five_letter_words = []
for word in words:
    filtered_word = re.sub(r'[^a-zA-Z]', '', word)
    if len(str(filtered_word)) == 5 and filtered_word not in five_letter_words:
        five_letter_words.append(filtered_word)

# Count each letter

frequency_table = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

for word in five_letter_words:
    for key in frequency_table:
        if key in word:
            frequency_table[key] = frequency_table[key] +1

final_table = sorted(frequency_table.items(), key=lambda item: item[1], reverse=True)

# Score each word
winners = []

def score_word(word):
    score = 0
    for x, y in final_table[:depth]:
        if x in word:
            score = score + 1
    return score

def check_anagram(word1, word2):
    if(sorted(word1) == sorted(word)):
        return True
    else:
        return False
    
for word in five_letter_words:
    anagram = False
    word_score = score_word(word)
    if word_score == 5:
        if len(winners) == 0:
            winners.append(word)
        else:
            for winner in winners:
                result = check_anagram(word, winner)
                if not result:
                    anagram = True
                    print(word, winner)
            if not anagram:
                winners.append(word)
