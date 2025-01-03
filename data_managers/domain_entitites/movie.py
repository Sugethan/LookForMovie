class story_infos():
    def __init__(self, title: str, plot: str, genres: str):
        self.title = title
        self.plot = plot
        self.genres = genres
        
class meta_infos():
    def __init__(self, director: str, cast: str, production: str, language: str, year: int):
        self.director = director
        self.cast = cast
        self.prodution = production
        self.language = language
        self.year = year
        
class reception_infos():
    def __init__(self, rating: int, awards: int):
        self.rating = rating
        self.awards = awards

class movie():
    def __init__(self, id: str, story_infos: story_infos, meta_infos: meta_infos, reception_infos: reception_infos):
        self.id = id
        self.story_infos = story_infos
        self.meta_infos = meta_infos
        self.reception_infos = reception_infos
    