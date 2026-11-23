class Codec:
    PREFIX = "http://tinyurl.com/"

    def __init__(self):
        self.id_to_url = {}
        self.url_to_id = {}
        self.next_id = 0

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.url_to_id:
            self.url_to_id[longUrl] = self.next_id
            self.id_to_url[self.next_id] = longUrl
            self.next_id += 1
        return self.PREFIX + str(self.url_to_id[longUrl])

    def decode(self, shortUrl: str) -> str:
        return self.id_to_url[int(shortUrl[len(self.PREFIX):])]
