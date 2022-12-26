from dataclasses import dataclass


@dataclass
class CuttingMethod:
    name: str
    url: str


@dataclass
class Recipe:
    name: str
    url: str


@dataclass
class Product:
    name: str
    cat: str
    description: str
    image_url: str
    recipes: list[str]
    cutting_methods: list[CuttingMethod]

products = [
    Product(
        'apple', 
        'fruit', 
        'A red fruit, very nice tasting. Originates from NL.',
         'https://media.istockphoto.com/id/184276818/nl/foto/red-apple.jpg?s=612x612&w=0&k=20&c=SX8NohTBbDQ1Tz50uFjuwr0EAuYXqgzIbZuwi94i3bw=', 
         [
            Recipe(
                'French apple tart',
                'https://www.bbcgoodfood.com/recipes/french-apple-tart'
            ),
            Recipe(
                'Next level apple crumble',
                'https://www.bbcgoodfood.com/recipes/next-level-apple-crumble'
            )
         ], 
         [
            CuttingMethod(
                'Julienne',
                'https://www.youtube.com/watch?v=sPTIQX7iP-Q',
            ),
            CuttingMethod(
                'Slices',
                'https://www.youtube.com/watch?v=H_M5cgWIQZU'
            )
        ]
    ),
    Product(
        'tomato', 
        'vegetable', 
        'A red vegetable. Commonly used for salads and on burgers.', 
        'https://t4.ftcdn.net/jpg/02/32/98/31/360_F_232983161_9lmUyHKnWbLW0vQPvWCrp5R5DSpexhbx.jpg', 
        [
            Recipe(
                'Tomato soup',
                'https://www.olivemagazine.com/recipes/healthy/dutch-tomato-soup/'
            ),
            Recipe(
                'Caprese salad',
                'https://www.olivemagazine.com/recipes/vegetarian/caprese-salad/'
            )
        ], 
        [
            CuttingMethod(
                'Slice',
                'https://www.youtube.com/watch?v=T0xVthFSJBg'
            ),
            CuttingMethod(
                'Core',
                'https://www.youtube.com/watch?v=dDt0L1-SaRg'
            )
        ]
    )
]
    