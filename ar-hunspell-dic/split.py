text = open('words_copy.ar', encoding='utf-8').read()

sections = text.split('#::::::::::::::')
print(len(sections))

names = [
    'stopwords.dic',
    'tools.dic',
    'names.dic',
    'verb.huns.dic'
]

for name, section in zip(names, sections):
    with open(name, mode='w', encoding='utf-8') as file_writer:
        file_writer.write(section)
