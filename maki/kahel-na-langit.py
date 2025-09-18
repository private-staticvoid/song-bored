import time
import sys

lyrics = [
    # Replace these with your own lines and timing
    ("Tensiyonado, nagulat din ako", 1.6, 0.13),
    ("No'ng malaman na hindi lang pala ako", 2.0, 0.15),
    ("'Yong nanghinayang no'ng nag-away tayo no'n", 2.1, 0.18),
    ("At natuluyan sa iyakan at tampo", 0.7, 0.15)
]

def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, line_delay, char_delay in lyrics:
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    print("Now playing: Tensionado (Soapdish)\n")
    play_lyrics(lyrics)

