#this function returns the vowels, consonants and numbers in a sentence.
import re

def search(sentence):
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    consonantRegex = re.compile(r'[^aeiouAEIOU0-9]')
    numberRegex = re.compile('\d+')

    vowels = vowelRegex.findall(sentence)
    consonants = consonantRegex.findall(sentence)
    numbers = numberRegex.findall(sentence)

    print(f'The vowels are: {vowels}')
    print(f'The consonants are: {consonants}')
    print(f'The numbers are: {numbers}')

my_sentence = 'Today is the last day of November, 2020.'
search(my_sentence)

