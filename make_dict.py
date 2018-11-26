def mkdict(addr):

    dict = {}

    f = open(addr)
    for line in f:
        words = line.split(":")
        dict[words[0].strip()] = words[1].strip()

    return dict

