import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('''INSERT INTO movies (id, title, director, rate, movie_description, trailer_url, image_url) VALUES (1, 'The Shawshank Redemption', 'Frank Darabont', '9.3', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', '/static/TheShawshankRedemption/TheShawshankRedemption.mpd', 'https://s4.uupload.ir/files/mv5bmdfkytc0mgetzmnhmc00zdizlwfmntetodm1zmrlywmwmwfmxkeyxkfqcgdeqxvymtmxodk2otu_._v1__mjaw.jpg')''')

cur.execute('''INSERT INTO movies (id, title, director, rate, movie_description, trailer_url, image_url) VALUES (2, 'The Godfather', 'Francis Ford Coppola', '9.2', 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.', '/static/TheGodfather/TheGodfather.mpd', 'https://s4.uupload.ir/files/mv5bm2mynjyxnmutytawni00mtyxlwjmnwytyzzlody3ztk3otflxkeyxkfqcgdeqxvynzkwmjq5nzm_._v1__pbhz.jpg')''')


cur.execute('''INSERT INTO movies (id, title, director, rate, movie_description, trailer_url, image_url) VALUES (3, 'The Dark Knight', 'Christopher Nolan', '9.0', 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', 'https://mm-fp-dash.arvanvod.com/5PxzR8rBXm/pBywnp3Ez9/h_,144_200,240_400,360_800,480_1469,k.mp4.list/manifest.mpd', 'https://s4.uupload.ir/files/mv5bmtmxntmwodm0nf5bml5banbnxkftztcwodaymtk2mw_._v1__bpsi.jpg')''')

cur.execute('''INSERT INTO movies (id, title, director, rate, movie_description, trailer_url, image_url) VALUES (4, 'The Godfather Part II', 'Francis Ford Coppola', '9.0', 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.', 'https://mm-fp-dash.arvanvod.com/5PxzR8rBXm/eoxpzwyO8R/h_,144_200,240_400,360_800,480_1500,k.mp4.list/manifest.mpd', 'https://s4.uupload.ir/files/mv5bmwmwmgqzztity2jlnc00owzilwiymdctndk2zdq2yjrjmwq0xkeyxkfqcgdeqxvynzkwmjq5nzm_._v1__cay.jpg')''')

cur.execute('''INSERT INTO movies (id, title, director, rate, movie_description, trailer_url, image_url) VALUES (5, '12 Angry Men', 'Sidney Lumet', '9.0', 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.', 'https://mm-fp-dash.arvanvod.com/5PxzR8rBXm/59wRG8MjZy/h_,144_200,240_400,360_800,480_1500,k.mp4.list/master.m3u8', 'https://s4.uupload.ir/files/mv5bmwu4n2fjnzytntvknc00nzq0ltg0mjatytjlmjfhnguxzdfmxkeyxkfqcgdeqxvynjc1ntyymjg_._v1__37s7.jpg')''')

cur.execute('''INSERT INTO movies (id, title, director, rate, movie_description, trailer_url, image_url) VALUES (6, 'Schindlers List', 'Steven Spielberg ', '9.0', 'In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.', 'https://mm-fp-dash.arvanvod.com/5PxzR8rBXm/7B1RWBa8Ln/h_,144_200,240_400,360_800,480_1458,k.mp4.list/master.m3u8', 'https://s4.uupload.ir/files/mv5bnde4otmxmtctnmrhyy00nwe2ltg3yzitytk3m2uwotu5njg4xkeyxkfqcgdeqxvynju0otq0oty_._v1__rw20.jpg')''')


connection.commit()
connection.close()
