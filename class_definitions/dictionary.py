# Zachary Hayes
import requests
import json


class Dictionary:
    '''Dictionary class provides random words from an API.'''

    def get_random_word(self):
        r = requests.get('https://random-word-api.herokuapp.com/word?number=1')
        array = json.loads(r.text)
        return array[0]
