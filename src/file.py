import pygame
import os.path
import pygame.display
import settings
import json
from pathlib import Path

def load_image(file_name, file_path = settings.ASSETS_FOLDER):
    #loads image from file system and returns it, returns False if not found
    full_file = os.path.join(file_path, file_name)
    try:
        my_abs_path = Path(full_file).resolve(strict=True)
    except:
        full_file = '/home/FingerTwister/assets/fingertwistererror.png'
        img = pygame.image.load(full_file)
    else:
        img = pygame.image.load(full_file)
    return img

def save_image(image, file_name, file_path = settings.ASSETS_FOLDER):
    pygame.image.save(image, file_path + "/" + file_name)
    print("Image", file_name, "saved successfully")

def load_json(file_name, file_path = settings.ASSETS_FOLDER):
    #loads json file, parses it into python object, and returns python object, returns False if not found
    full_file = os.path.join(file_path, file_name)
    try:
        my_abs_path = Path(full_file).resolve(strict=True)
    except:
        full_file = '/home/FingerTwister/assets/leaderboard.json'
    json_data = open(full_file)
    data = json.load(json_data)
    return data

def save_json(json_data, file_name, file_path = settings.ASSETS_FOLDER):
    #saves python object to json file, returns if successful or not
    full_file = os.path.join(file_path, file_name)
    try:
        my_abs_path = Path(file_path).resolve(strict=True)
    except:
        print('Not a valid path')
    else:
        with open(full_file, 'w') as f:
            json.dump(json_data, f)
        print('File ' + file_name + ' saved succesfully')

