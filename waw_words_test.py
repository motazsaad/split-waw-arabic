import re

from process_waw_rooting_ayspell import separate_waw_word

# from process_waw_rooting_hunspell import separate_waw_word


arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)


def remove_diacritics(text):
    text = re.sub(arabic_diacritics, '', text)
    return text


infile = open('waw_words.txt', encoding='utf-8')
words = [remove_diacritics(word) for word in infile.read().split() if len(remove_diacritics(word)) > 2]

for word in words:
    print(word)
    new_word = separate_waw_word(word)
    if new_word != word:
        print('{} changed to {}'.format(word, new_word))
