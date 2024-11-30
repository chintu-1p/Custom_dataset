import numpy as np

Anime = np.dtype([
    ('Name', 'U20'),
    ('Genre', 'U40'),
    ('Rating', 'f8')
])

Anime_Details = np.array([
    ('One Piece', 'Adventure,Action,Comedy', 9.0),
    ('Bleach', 'Action,Comedy,Thriller', 8.5),
    ('Death Note', 'Thriller,Action,Horror', 9.5),
    ('Haikyuu', 'Sports,Comedy', 9.0),
    ('Tomodachi Game', 'Thriller,Action,Psychological', 7.5)
], dtype=Anime)

print(Anime_Details)
print('Name: ', Anime_Details['Name'])
print('Genre: ', Anime_Details['Genre'])
print('Rating: ', Anime_Details['Rating'])
