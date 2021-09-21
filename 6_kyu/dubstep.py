# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python

def song_decoder(song):
    for wub in song:
        song = song.replace('WUB', ' ')
    return ' '.join(song.split())


print(song_decoder('AWUBBWUBC'))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder('WUBAWUBBWUBCWUB'))

