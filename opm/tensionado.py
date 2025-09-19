import time
import sys

# ANSI escape codes for yellow text
YELLOW = "\033[93m"
RESET = "\033[0m"

lyrics = [
    ("Nagulat din ako", 0.15),
    ("No'ng malaman na hindi lang pala ako", 0.15),
    ("'Yung nanghinayang no'ng nag-away tayo noon", 0.15),
    ("At natuluyan sa iyakan at tampo", 0.17),
    ("At sandali lang", 0.16),
    ("Wag ka munang magsalita", 0.15),
    ("Di ko hahayaan lahat ito ay mawala", 0.15),
    ("Ang iniisip ko", 0.18),
    ("Kung pwede pa ba tayo?", 0.10),
]

# Delays between lines (seconds pause after each line)
delays = [
    0.4,  # after "Nagulat din ako"
    0.6,  # after "No'ng malaman na hindi lang pala ako"
    0.9,  # after "'Yung nanghinayang no'ng nag-away tayo noon"
    1.2,  # after "At natuluyan sa iyakan at tampo"
    0.7,  # after "At sandali lang"
    0.4,  # after "Wag ka munang magsalita"
    0.7,  # after "Di ko hahayaan lahat ito ay mawala"
    0.7,  # after "Ang iniisip ko"
    0.4,  # after "Kung pwede pa ba tayo?"
]

def play_lyrics(lyrics, delays):
    for i, (line, char_delay) in enumerate(lyrics):
        # Print characters one by one
        for char in line:
            sys.stdout.write(f"{YELLOW}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(char_delay)
        sys.stdout.write("\n")
        sys.stdout.flush()

        # Pause after the line
        if i < len(delays):
            time.sleep(delays[i])

if __name__ == "__main__":
    print(f"{YELLOW}Now playing...{RESET}\n")
    play_lyrics(lyrics, delays)


#tensionado, timing of the song, lyrics, yellow text, delays, character-by-character display