addr = r"F:\Movies\# Series\Friends\S01\friends--first-season_HI_english-842737\friends.s01e01.720p.bluray.x264-psychd.srt"

f = open(addr)

f.readline()  #some weird characters around 1st line indicator
for line in f:
    words = line.split()
    if len(words) == 1:
        try:
            print(int(words[0]))
        except:
            pass