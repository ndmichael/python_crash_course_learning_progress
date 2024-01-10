def make_album(artiste, title, num_of_songs=None):
    album = {"artiste": artiste, "title": title}    

    if num_of_songs:
        album['songs'] = num_of_songs
    return album


flag = True

while flag:
    artiste_name = input("Enter the artiste name: ")
    title = input("Enter the title: ")
    songs = input("Number of songs: ")
    album = make_album(artiste_name, title, songs)
    print(f"{album}", end="\n\n")

    choice = input("enter q to quite: ")
    if choice.lower() == 'q':
        break


