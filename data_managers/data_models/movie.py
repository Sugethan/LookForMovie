from pydantic import BaseModel, model_validator
from typing import Any, List

class story_infos_model(BaseModel):
    title: str
    plot: str
    genres: List[str]
    
class meta_infos_model(BaseModel):
    director: List[str]
    cast: List[str]
    production: str
    language: List[str]
    year: int
    
class reception_infos_model(BaseModel):
    rating: int
    awards: int

class movie_model(BaseModel):
    id: str
    story_infos: story_infos_model
    meta_infos: meta_infos_model
    reception_infos: reception_infos_model
    
    @model_validator(mode="before")
    def map_logins(cls, data: dict[str, Any]):
        
        data["story_infos"] = {
            "title": data.pop("title", None),
            "plot": data.pop("plot", None),
            "genres": data.pop("genres", None),
        }
        
        data["meta_infos"] = {
            "director": data.pop("director", None),
            "cast": data.pop("cast", None),
            "production": data.pop("production", None),
            "language": data.pop("language", None),
            "year": data.pop("year", None),
        }
        
        data["id"] = data.get("_id", dict()).get("$oid", None)
        data.pop("_id", None)
        
        tomatoes_rating = int(data.get("tomatoes", dict()).get("rating", 0))
        imdb_rating = int(data.get("imdb", dict()).get("rating", 0))
        data["reception_infos"] = {
            "awards": data.get("awards", dict()).get("wins", 0),
            "rating": (tomatoes_rating* 2 + imdb_rating) / 2,
        }
        data.pop("awards", None)
        data.pop("tomatoes", None)
        data.pop("imdb", None)
        
            
        return data