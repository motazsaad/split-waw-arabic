import argparse

from nltk.stem.isri import ISRIStemmer


def load_lex(file_name):
    lines = open(file_name, encoding='utf-8').read().split('\n')
    words = list()
    for line in lines:
        if line.startswith(':') or line.startswith('#'):
            continue
        if line.strip():
            words.append(line.strip())
    return tuple(words)


# ar_spell = aspell.Speller(('dict-dir', './ar_ayspell_dict/'),
#                           ('lang', 'ar'),
#                           ('encoding', 'utf-8'))

hunspell = load_lex('./ar-hunspell-dic/words.ar')


def get_root_word(arabic_word):
    arabic_stemmer = ISRIStemmer()
    arabic_root = arabic_stemmer.stem(arabic_word)
    return arabic_root


def separate_waw_word(word):
    if word.startswith('و'):
        root = get_root_word(word[1:])
        # print(root)
        if root in hunspell:
            print(root, 'root in dictionary')
            return 'و ' + word[1:]
        else:
            print('root not in dictionary ')
            return word
    else:
        return word


def separate_waw(text):
    words = inline.split()
    sentence = ''
    for word in words:
        new_word = separate_waw_word(word)
        sentence += new_word + ' '
        if new_word != word:
            print('{} changed to {}'.format(word, new_word))

    return sentence


parser = argparse.ArgumentParser(description='separate the '
                                             'conjunction waw from '
                                             'Arabic words')

parser.add_argument('-i', '--infile', type=argparse.FileType(mode='r', encoding='utf-8'),
                    help='input file.', required=True)
parser.add_argument('-o', '--outfile', type=argparse.FileType(mode='w', encoding='utf-8'),
                    help='out file.', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    inlines = args.infile.readlines()
    clean_lines = list()
    for inline in inlines:
        clean_lines.append(separate_waw(inline))
    args.outfile.write('\n'.join(clean_lines))
