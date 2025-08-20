import pygame
from typing import List
import settings

path = settings.ASSETS_FOLDER

class Sound:
    def __init__(self):
        pass

    #call first
    def _initialize_sound_engine(self):
        pygame.mixer.init()

    def close_sound_engine(self):
        pygame.mixer.quit()

    def _load_sound(self, filename: str):
        sound = pygame.mixer.Sound(file = filename)
        return sound

    #input = string list of filenames, returns dictionary of (str, pygame.mixer.sound)
    def load_all_sounds(self, sound_name_list: List[str]):
        sound_dictionary = {}
        self.initialize_sound_engine()

        for sound_name in sound_name_list:
            sound = self.load_sound(path + sound_name)
            sound_dictionary[sound_name] = sound

        return sound_dictionary

    #input = sound name
    def play_sound_once(self, sound: pygame.mixer.Sound):
        channel = sound.play()
        return channel

    #input = sound name
    def play_sound_infinite_repeat(self, sound: pygame.mixer.Sound):
        ch = sound.play(loops = -1)
        return ch

    #input = sound name, time in ms
    #def play_sound_with_fadeout(self, sound: pygame.mixer.Sound, time: int):
    #    channel = self.play_sound_once(sound)
    #    while 
    #    sound.fadeout(time)
    #    return channel

    #stops all sound with no ability to restart where it stopped
    def stop_all_sound(self):
        pygame.mixer.stop()

    #stops all sound with the ability to resume with unpause
    def pause_all_sound(self):
        pygame.mixer.pause()

    #restores sound from pause
    def unpause_all_sound(self):
        pygame.mixer.unpause()

    #sets volume range 0 to 1
    def set_volume(self, amount: float):
        pygame.mixer.Sound.set_volume(amount)

if __name__ == "__main__":
    #create instanace
    sound = Sound()
    #list of filenames
    sounds = ["test.mp3", "meow.mp3", "technokitty.mp3"]
    #load all sounds to a dict(str, pygame.mixer.Sound)
    output = sound.load_all_sounds(sounds)
    #plays a sound, we wait on the channel here to test the file solo
    ch = sound.play_sound_once(output["test.mp3"])
    #I'm guessing the regular game running will make this irrelevant
    while ch.get_busy():
        pygame.time.wait(1000)

    ch = sound.play_sound_once(output["meow.mp3"])
    while ch.get_busy():
        pygame.time.wait(1000)
