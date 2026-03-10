
class Track:
    def __init__(self, name, location):
        self.name = name
        self.location = location
def read_tracks(music_file):
    count = int(music_file.readline().strip())
    tracks = []
    index = 0
    while index < count:
        track = read_track(music_file)
        tracks.append(track)
        index += 1  
    return tracks

def read_track(music_file):
    name = music_file.readline().strip()
    location = music_file.readline().strip()
    return Track(name, location)

def print_tracks(tracks):
    index = 0
    while index < len(tracks):
        print_track(tracks[index])
        index += 1

def print_track(track):
    print(f"Track Name: {track.name}")
    print(f"Track Location: {track.location}")

def main():
    music_file = open("input.txt", "r")
    tracks = read_tracks(music_file)
    music_file.close()
    print_tracks(tracks)

main()


