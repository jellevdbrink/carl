from dataclasses import dataclass

@dataclass
class Product:
    name: str
    image_url: str
    recipes: list[str]
    videos: list[str]
    