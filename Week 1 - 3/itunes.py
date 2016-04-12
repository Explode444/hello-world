import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('C:\Users\jordan.frank\Desktop\python\Class\Week 1 - 3\itunes.sqlite')
cur = conn.cursor()
file_name = "C:\Users\jordan.frank\Desktop\python\Class\Week 1 - 3\Library.xml"
data = ET.parse(file_name)
all = data.findall("dict/dict/dict")
print "Dict Count:", len(all)

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


for entry in all:
    if lookup(entry, "Track ID") is None:
        continue
    track = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    genre = lookup(entry, "Genre")
    length = lookup(entry, "Total Time")
    rating = lookup(entry, "Rating")
    count = lookup(entry, "Play Count")

    
   # print track, artist, album, genre, length, rating    
    if track is None or artist is None or album is None:
        continue
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]
    if genre is not None:
        cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', (genre, ))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
        genre_id = cur.fetchone()[0]
    else:
        genre_id = None
   
    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?, ?)''', (track, album_id, genre_id, length, rating, count))
        
    conn.commit()    