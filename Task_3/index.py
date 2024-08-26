import lyricsgenius

token = "zMxKB6bUCugbTBXB3OaakC_1K47CpmsxSCyaJR_FmFqnaNX1g4K7av2INaApbknT"
genius = lyricsgenius.Genius(token)

artist = genius.search_artist("Eminem", max_songs=10, sort="title")
print(artist.songs)

song = genius.search_song("Lose Yourself", "Eminem")
print(song.lyrics)
