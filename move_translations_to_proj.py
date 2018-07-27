'''
 Moves translated values to the project
'''

import os
import json

from shared import app_root, locales
from shared import save, read_obj, get_translations

dirs_to_walk = ['scenes', 'components', 'services']


def walk():
    translations = get_translations(locales)
    try:
        for dir in dirs_to_walk:
            for root, dirs, files in os.walk(os.path.join(app_root, dir)):
                for file in files:
                    file_name = file.split('.')[0]
                    if file_name in locales:
                        path = os.path.join(root, file)
                        obj = read_obj(path)
                        for key in translations[file_name]:
                            if key in obj:
                                obj[key] = translations[file_name][key]
                        save(obj, path)

    except Exception as e:
        print(str(e) + " " + path)


def copy():
    for dir in dirs_to_walk:
        for root, dirs, files in os.walk(os.path.join(app_root, dir)):
            for file in files:
                file_name = file.split('.')[0]
                if file_name == 'en':
                    path = os.path.join(root, file)
                    data = read_obj(path)
                    for locale in locales:
                        if locale != 'en':
                            save(data, os.path.join(root, locale + '.json'))

if __name__ == '__main__':
    walk()