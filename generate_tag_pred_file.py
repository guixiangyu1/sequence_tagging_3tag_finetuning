# 输入tags，得到相应的实体块
def get_chunk(tags):
    chunk = []
    chunk_start = None
    pre = "O"
    for i,tag in enumerate(tags):
        if tag == 'B':
            if chunk_start != None:
                chunk.append((chunk_start,i))
            chunk_start = i
        if tag == "I":
            pass
        if tag == "O":
            if chunk_start != None:
                chunk.append((chunk_start,i))
            chunk_start = None
    if chunk_start != None:
        chunk.append((chunk_start, len(tags)))
        chunk_start = None
    return chunk



# 将test.txt与预测的tag_pred合成为一个文件
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


#将合成后的文件处理成classification需要的形式，onebyone
words, tags = [], []
with open("results/To_be_classified.txt") as f:
    g = open("results/For_onebyone.txt", 'w')
    for line in f:
        line = line.strip()
        if len(line)==0 or line.startswith("-DOCSTART-"):
            if len(tags)!=0:
                chunk = get_chunk(tags)
                for (chunk_start, chunk_end) in chunk:
                    for i, (one_word, one_tag) in enumerate(zip(words, tags)):
                        if i<chunk_start or i>=chunk_end:
                            g.write("{} O\n".format(one_word))
                        else:
                            g.write("{} {}\n".format(one_word, one_tag))
                    g.write("\n")

        else:
            word = line.split(' ')[0]
            tag  = line.split(' ')[-1]
            words += [word]
            tags  += [tag]
    g.close()






