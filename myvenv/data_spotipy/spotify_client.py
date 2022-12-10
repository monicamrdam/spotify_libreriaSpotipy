
class Artist:
    def __init__(self, name: str, popularity: int, uri: str):
        self.name=name
        self.popularity = popularity
        self.uri=uri



class Song:
    def __init__(self, ranking: int, name:str, author:str, date: str, countrhy:str):
        self.ranking=ranking
        self.name=name
        self.author=author
        self.date=date
        self.country=country


