
with open("results/To_be_classified.txt","w") as f:
    with open("data/test.txt") as g:
        h = open("results/tag_pred.txt")
        for raw_text_line in g:
            if raw_text_line=="\n" or raw_text_line.startswith("-DOCSTART-"):
                f.write(raw_text_line)
            else:
                # if len(raw_text_line.strip())!=0:
                tag = h.readline()
                while (tag == '\n'):
                    tag = h.readline()
                raw_text_line = raw_text_line.strip()
                f.write("{} {}".format(raw_text_line, tag))
        h.close()





