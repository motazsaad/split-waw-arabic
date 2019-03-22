import argparse
import aspell

# ar_spell = aspell.Speller('lang', 'ar')
ar_spell = aspell.Speller(('dict-dir', './ar_ayspell_dict/'),
                          ('lang', 'ar'),
                          ('encoding', 'utf-8'))


def separate_waw(text):
    words = line.split()
    sentence = ''
    for word in words:
        if word.startswith('و'):
            if word in ar_spell:
                sentence += word + ' '
            else:
                sentence += 'و ' + word[1:] + ' '
                print('{} changed to {}'.format(word, 'و ' + word[1:]))
        else:
            sentence += word + ' '
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
    lines = args.infile.readlines()
    clean_lines = list()
    for line in lines:
        clean_lines.append(separate_waw(line))
    args.outfile.write('\n'.join(clean_lines))
