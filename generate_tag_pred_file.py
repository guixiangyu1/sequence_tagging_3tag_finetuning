
with open("results/To_be_classified.txt","w") as f:
    g = open("data/test.txt")
    h = open("results/tag_pred.txt")
    while (1):
        raw_text_line = g.readline()
        tag = h.readline()
        while(tag=='\n'):
            tag = h.readline()


        if raw_text_line=="\n" or raw_text_line.startswith("-DOCSTRAT-"):
            f.write(raw_text_line)
        if raw_text_line=='':
            break
        if len(raw_text_line.strip())!=0:
            raw_text_line = raw_text_line.strip()
            f.write("{} {}".format(raw_text_line, tag))
    g.close()
    h.close()





