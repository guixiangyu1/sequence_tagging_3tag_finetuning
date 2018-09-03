
with open("filname","w") as f:
    g = open("file1")
    h = open("file2")

    raw_text_line = g.readline()
    tag = h.readline()
    while(tag=='\n'):
        tag = h.readline()


    if raw_text_line=="\n" or raw_text_line.startswith("-DOCSTRAT-"):
        f.write(raw_text_line)
    else:
        raw_text_line = raw_text_line.strip()
        f.write("{} {}".format(raw_text_line, tag))
    g.close()
    h.close()





