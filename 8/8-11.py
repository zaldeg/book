magicians = ['Mark', 'Shelby', 'Zil', 'Pendalf']


def show_magicians(mags):
    for mag in mags:
        print(mag)


def make_great(mags):
    for mag in mags:
        mags.remove(mag)
        mags.insert(0, 'Great ' + mag)
    return mags


show_magicians(magicians)
a = make_great(magicians[:])
show_magicians(magicians)
show_magicians(a)
print(magicians)

