from requests import get
import json

class Client:
    def __init__(self):
        try:
            with open('offsets.json') as f:
                self.offsets = json.load(f)
            self.clientdll = get('https://raw.githubusercontent.com/a2x/cs2-dumper/main/generated/client.dll.json').json()
        except:
            print('Unable to get offsets.')
            exit()

    def offset(self, a):
        try:
            return self.offsets['client_dll']['data'][a]['value']
        except:
            print(f'Offset {a} not found.')
            exit()

    def get(self, a, b):
        try:
            return self.clientdll[a]['data'][b]['value']
        except:
            print(f'Unable to get {a}, {b}.')
            exit()