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
    certainty: float
    image_url: str
    recipes: any
    cutting_methods: any

products = [
    Product(
        name='apple', 
        cat='fruit', 
        description='A red fruit, very nice tasting. Originates from NL.',
        certainty=0.635,
        image_url='https://media.istockphoto.com/id/184276818/nl/foto/red-apple.jpg?s=612x612&w=0&k=20&c=SX8NohTBbDQ1Tz50uFjuwr0EAuYXqgzIbZuwi94i3bw=', 
        recipes=[
            Recipe(
                'French apple tart',
                'https://www.bbcgoodfood.com/recipes/french-apple-tart'
            ),
            Recipe(
                'Next level apple crumble',
                'https://www.bbcgoodfood.com/recipes/next-level-apple-crumble'
            )
        ], 
        cutting_methods=[
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
        name='Tomato', 
        cat='vegetable', 
        description='A red vegetable. Commonly used for salads and on burgers.',
        certainty=0.929,
        image_url='https://t4.ftcdn.net/jpg/02/32/98/31/360_F_232983161_9lmUyHKnWbLW0vQPvWCrp5R5DSpexhbx.jpg', 
        recipes=[
            Recipe(
                'Tomato soup',
                'https://www.olivemagazine.com/recipes/healthy/dutch-tomato-soup/'
            ),
            Recipe(
                'Caprese salad',
                'https://www.olivemagazine.com/recipes/vegetarian/caprese-salad/'
            )
        ], 
        cutting_methods=[
            CuttingMethod(
                'Slice',
                'https://www.youtube.com/watch?v=T0xVthFSJBg'
            ),
            CuttingMethod(
                'Core',
                'https://www.youtube.com/watch?v=dDt0L1-SaRg'
            )
        ]
    ),
    Product(
        'Banana', 
        'fruit', 
        'A yellow fruit. Very nice in smoothies and on pancakes', 
        0.829,
        'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Banana-Single.jpg/2324px-Banana-Single.jpg', 
        [
            Recipe(
                'Banana Smoothie',
                'https://kristineskitchenblog.com/banana-smoothie/'
            )
        ], 
        [
            CuttingMethod(
                'Slice',
                'https://www.youtube.com/watch?v=Fr3YBORM3eE'
            )
        ]
    ),
    Product(
        'Bell pepper', 
        'vegetable', 
        'A red vegetable. Can be used everywhere', 
        0.456,
        'https://i5.walmartimages.com/asr/7be94a8e-9a5d-4f87-842f-5fe4084138ba.c95d36e140f5e0d492ca632b42e4543c.jpeg', 
        [
            Recipe(
                'Quinoa',
                'https://foodnetwork.co.uk/recipes/cucumber-bell-pepper-quinoa'
            ),
            Recipe(
                'Mexican stuffed',
                'https://www.tasteofhome.com/recipes/mexican-stuffed-peppers/'
            )
        ], 
        [
            CuttingMethod(
                'Slice',
                'https://www.youtube.com/watch?v=hZGqtmwboHU'
            )
        ]
    )
]
    