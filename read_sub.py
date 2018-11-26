def read_subtitle(addr, dict):
    f = open(addr)
    new_sub = ""
    for line in f:
        words = line.split()
        for w in words:
            if w in dict:
                new_sub += " " + w + "(" + dict[w] + ")"
            else:
                new_sub += " " + w
        print("\n")
    return new_sub