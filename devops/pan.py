

import string

def is_pangram(sentence):
    sentence = sentence.lower()
    return all(letter in sentence for letter in string.ascii_lowercase)

sentence = input("Enter a string: ")
print(is_pangram(sentence))
