def read_subtitle(addr):
    f = open(addr)
    f.readline()  #some weird characters around 1st line indicator
    for line in f:
        words = line.split()
        if len(words) == 1:
            try:
                print(int(words[0]))
            except:
                pass
    return "file read"