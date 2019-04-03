class JsonDict:
    def __init__(self, json):
        self.json=json

    def __getattr__(self, key):
        return self.json[key]

    def __getitem__(self, key):
        return self.json[key]
        
    def __repr__(self):
        return str(self.json)
