from parsers.song_parser import parse_song_names
from searches.web_searcher import search_and_handle
from config import SEARCH_URL, SOURCE_URL
def main():
    songs = parse_song_names(SOURCE_URL)
    if not songs:
        print("Не удалось найти названия песен")
        return
    print("Найденные песни:", songs)
    for song in songs:
        search_and_handle(song, SEARCH_URL)

if __name__ == "__main__":
    main()