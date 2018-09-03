f = open("data/test.txt")
g = open("data/chunk.txt")

with open("data/test.txt") as f:
    words = []
    all_words = []
    for line in f:
        line = line.strip()
        if (len(line) == 0 or line.startswith("-DOCSTART-")):
            if len(words) != 0:
                all_words += [words]
                words = []
        else:
            words += [line.split(' ')[0]]
    if len(words) != 0:
        all_words += [words]
        words = []


all_tags = []
tags = []
with open("data/chunk.txt") as g:
    for line in g:
        line = line.strip()
        if len(line) == 0:
            if len(tags) != 0:
                all_tags += [tags]
                tags = []
        else:
            tags += [line.split(' ')[0]]
    if len(tags) != 0:
        all_tags += [tags]
        tags = []

with open("data/transit.txt","w") as h:
    for words, tags in zip(all_words, all_tags):
        for word, tag in zip(words, tags):
            if tag == "O":
                h.write("{} {}\n".format(word, tag))
            else:
                h.write("{} {}-LOC\n".format(word, tag))
        h.write("\n")


