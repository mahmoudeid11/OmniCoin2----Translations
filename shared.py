import os
import json

translations_root = os.getcwd()
locales_root = '/Users/denissamohvalov/Documents/scopic-development/omnibazaar-ui/app/dist/i18n/app'
app_root = '/Users/denissamohvalov/Documents/scopic-development/omnibazaar-ui/app'
locales = ['en', 'es', 'fr', 'it', 'ru']


def save(obj, path):
    with open(path, 'w') as out:
        out.write(json.dumps(obj, indent=2))


def read_obj(path):
    with open(path, 'r') as stream:
        return json.loads(stream.read())


def get_translations(locales):
    translations = {}
    for locale in locales:
        with open(os.path.join(translations_root, '%s.json' % locale)) as json_data:
            translations[locale] = json.loads(json_data.read())
    return translations
