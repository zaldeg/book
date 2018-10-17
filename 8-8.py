def make_album(name, album, tracks=''):
    albums = dict()
    if tracks:
        albums[name.title()] = (album.title(), tracks)
    else:
        albums[name.title()] = album.title()
    return albums

result = dict()

while True:
    info_name = input('name\n')
    if info_name == 'q':
        break
    info_album = input('album\n')
    if info_album == 'q':
        break
    info_tracks = input('tracks\n')
    if info_tracks == 'q':
        break
    if info_tracks:
        a = make_album(info_name, info_album, info_tracks)
    else:
        a = make_album(info_name, info_album)
    result.update(a)

print(result)
