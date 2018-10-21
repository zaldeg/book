magicians = ['Mark', 'Shelby', 'Zil', 'Pendalf']


def show_magicians(mags):
    for mag in mags:
        print(mag)


def make_great(mags):
    for mag in mags:
        mags.remove(mag)
        mags.insert(0, 'Great ' + mag)


show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
print(magicians)

