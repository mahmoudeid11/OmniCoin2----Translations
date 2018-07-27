'''
    Moves locales from processed locales dir to Omnicoin Transaltions repo
'''
import os
import json

from shared import locales, translations_root, locales_root
from shared import save, read_obj, get_translations


def save_translations(translations):
    for i in range(len(locales)):
        path = os.path.join(translations_root, '%s.json' % locales[i])
        obj = translations[locales[i]]
        save(obj, path)


def walk():
    translations = get_translations(locales)
    try:
        for root, dirs, files in os.walk(locales_root):
            for file in files:
                path = os.path.join(root, file)
                data = read_obj(path)
                for el in data:
                    if el['id'] not in translations['en']:
                        for locale, translation in translations.items():
                            translation[el['id']] = el['defaultMessage']
    except Exception as e:
        print(str(e) + " " + path)
    save_translations(translations)


if __name__ == '__main__':
    walk()


