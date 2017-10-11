import requests

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE'
response = requests.get(url)

print (response.status_code)

class Data(object):
    def __init__(self, data_object):
        self.results = data_object ['results']

    def get_places(self):
        return self.results

    def get_place(self):
        return  Place(self.results[0])

class Place:
    def __init__(self, place):
        self.place = place
        self.icon = place ['icon']
        self.id = place ['id']
        self.name = place ['name']

    def get_icon(self):
        return self.icon

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name



prueba = Data(response.json())
print(Place.get_name())

