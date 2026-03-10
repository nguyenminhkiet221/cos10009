import input_functions 




class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location


def read_track(music_file):
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    return Track(name, location)


def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []
    index = 0
    while index < count:
        track = read_track(music_file)
        tracks.append(track)
        index += 1  
    return tracks

def print_tracks(tracks):
    index = 0
    while index < len(tracks):
        print_track(tracks[index])
        index += 1

def print_track(track):
    print(f"Track title is: {track.name}")
    print(f"Track file location is: {track.location}")

#=================================================================================




# search for track by name
# returns the index of the track or -1 if not found
search_string = input_functions.read_string("Enter the track name you want to find: ")
def search_for_track_name(tracks, search_string):
    # put a while loop here that searches through the tracks

    found_index = 0
    while found_index < len(tracks):
        if tracks[found_index].name.strip() == search_string.strip():
            return found_index
        found_index += 1

    # Use the read_string() function from input_functions.py to get the search string
    # NB: you might need to use .strip() to compare the strings correctly
    # put your code here.
    return found_index-1


#===============================================================

def print_track_founded(track, found_index):
    if found_index > -1:
        print(f"Found {track[found_index].name} at index {found_index}")
    else:
        print("Can't find the track")


def main():
    # Open the file using "with" to ensure it gets closed later
    with open("album.txt", "r") as music_file:
        tracks = read_tracks(music_file)
        print_tracks(tracks)

    search_string = input_functions.read_string("Enter the track name you wish to find: ")
    index = search_for_track_name(tracks, search_string)
    if index > -1:
        print(f"Found {tracks[index].name} at index {index}")
    else:
        print("Entry not found")