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
    recipes: any
    cutting_methods: any

products = [
    Product(
        name='apple', 
        cat='fruit', 
        description='A red fruit, very nice tasting. Originates from NL.',
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
        'Paprika',
        'vegetable', 
        'A red vegetable. Can be used everywhere',
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
    ),
    Product(
        name='Cucumber', 
        cat='vegetable', 
        description='A green vegetable. Long and used for a lot of things.',
        image_url='https://www.creedfoodservice.co.uk/media/catalog/product/cache/d781aa45b0623b3b1e7a18c482a05dd6/7/e/7e355a4b3ad12ed0d91c734d6022f097.jpg', 
        recipes=[
            Recipe(
                'Salad',
                'https://www.bbcgoodfood.com/recipes/tomato-cucumber-coriander-salad'
            )
        ], 
        cutting_methods=[
            CuttingMethod(
                'Chinese style',
                'https://www.youtube.com/watch?v=7cPRq-iEZis'
            ),
            CuttingMethod(
                'Sushi',
                'https://www.youtube.com/watch?v=GxK04UlYsZQ'
            )
        ]
    ),
    Product(
        name='Carrot', 
        cat='vegetable', 
        description='A orange vegetable. Long and used for a lot of things.',
        image_url='https://www.alimentarium.org/sites/default/files/media/image/2016-10/AL012-02%20carotte_0.jpg', 
        recipes=[
            Recipe(
                'Cake',
                'https://www.bbcgoodfood.com/recipes/yummy-scrummy-carrot-cake-recipe'
            ),
            Recipe(
                'Buttered',
                'https://www.bbcgoodfood.com/recipes/buttered-baby-carrots'
            )
        ], 
        cutting_methods=[
            CuttingMethod(
                'Dice',
                'https://www.youtube.com/watch?v=lzOTXFp2mwM'
            ),
            CuttingMethod(
                'Julienne',
                'https://www.youtube.com/watch?v=KGNKz1WAiFQ'
            )
        ]
    )
]

def find_product(prod_name):
    for prod in products:
        if prod.name.lower() == prod_name.lower():
            return prod
