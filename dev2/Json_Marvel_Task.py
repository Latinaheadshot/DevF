# coding=utf-8
import json

json_file = open('marvel.json').read()
json_data = json.loads(json_file)
print json_data['data']['results'][0]['comics']['items'][9]

class Data:
    def __init__(self):
        pass

class Result:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Thumbnail:
    def __init__(self, path, extension):
        self.path = path
        self.extension = extension

class Comic:
    def __init__ (self, available, items):
        self.avalaible = available
        self.collectionURI = collectionURI
        self.items = items

class Series:
    def __init__ (self, available, items):
        self.avalaible = available
        self.collectionURI = collectionURI
        self.items = items

class Stories:
    def __init__ (self, available, items):
        self.avalaible = available
        self.collectionURI = collectionURI
        self.items = items

class Events:
    def __init__ (self, available, items):
        self.avalaible = available
        self.collectionURI = collectionURI
        self.items = items

