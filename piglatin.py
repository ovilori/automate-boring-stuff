"""function of this program is to alter English words.
if a word begins with a vowel, 'yay' is added to the end of it.
if it begins with a consonant or cluster of consonants, (gh, by etc.), 
the consonant or cluster is moved to the end of it followed by 'ay'"""

message_to_modify = input('Enter the English message to be modified: ')
#list of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
#a list of the words in pig latin
pigLatin = []
for word in message_to_modify.split():
    #seperating the non leters at the start of each word
    nonLettersPrefix = ''
    while len(word) > 0 and not word[0].isalpha():
        nonLettersPrefix += word[0]
        word = word[1:]
    #append to pigLatin if the entire word does not have any letter.
    
    if len(word) == 0:
        pigLatin.append(nonLettersPrefix)
        continue
    #seperating the non leters at the end of each word
    nonLettersSuffix = ''
    while len(word) > 0 and not word[-1].isalpha():
        nonLettersSuffix += word[-1]
        word = word[:-1]
    #remembering the case of each word
    Upper = word.isupper()
    Title = word.istitle()

    #change the case of the word to lower case for translation
    word = word.lower()

    #seperating the consonants at the start of each word
    Prefixisconsonant = ''
    while len(word) > 0 and not word[0] in vowels:
        Prefixisconsonant += word[0]
        word = word[1:]

    #adding the pig latin to the word
    if Prefixisconsonant != '':
        word += Prefixisconsonant + 'ay'
    else:
        word += 'yay'
    #returning the word back to it's original case
    if Upper:
        word = word.upper()
    if Title:
        word = word.title()

    #adding the non letters back to the start or end of the word.

    pigLatin.append(nonLettersPrefix + word + nonLettersSuffix)

    #joining all the words back into a string
    translated_message = ' '.join(pigLatin)
    
#displaying the translated message
print(translated_message)