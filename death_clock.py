import time
import datetime
import pygame
import os

SOUND_FILE_1 = "sheep.mp3"
SOUND_FILE_2 = "countdown.mp3"
CHECK_INTERVAL_SECONDS = 1

def play_sound(file_path):
    if not os.path.exists(file_path):
        print(f"[{datetime.datetime.now()}] Error: Audio not found {file_path}")
        return

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"[{datetime.datetime.now()}] Playing: {file_path}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Error while playing audio: {e}")


def main():
    pygame.init()
    pygame.mixer.init()

    print("The death clock has been started.")
    print(f"at the 50th minute of every hour plays {SOUND_FILE_1}")
    print(f"every hour on the hour plays {SOUND_FILE_2}")

    last_played_minute = -1

    while True:
        try:
            current_time = datetime.datetime.now()
            current_minute = current_time.minute

            # Check if there is no play in this minute
            if current_minute != last_played_minute:
                if current_minute == 50:
                    play_sound(SOUND_FILE_1)
                    last_played_minute = current_minute

                elif current_minute == 0:
                    play_sound(SOUND_FILE_2)
                    last_played_minute = current_minute

            time.sleep(CHECK_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            # Ctrl+C
            print("\nThe program has stopped.")
            break
        except Exception as e:
            print(f"error occurred: {e}")
            time.sleep(10)  # Prevent repeated attempts


if __name__ == "__main__":
    main()
