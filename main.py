from read_sub import read_subtitle
from make_dict import mkdict

sub_addr = r"J:\Movies\# Series\Friends\S01\friends--first-season_HI_english-842737\friends.s01e01.720p.bluray.x264-psychd.srt"
dict_addr = r"G:\lang-with-movies\Dict\504.txt"

dict = mkdict(dict_addr)

new = read_subtitle(sub_addr, dict)

print("end")