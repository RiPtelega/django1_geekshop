import json, os
from mainapp.models import Product, ProductCategory

JSON_PATH = os.path.join('mainapp', 'json')


def load_from_json(filename):
    with open(os.path.join(JSON_PATH, filename), 'r') as json_file:
        return json.load(json_file)


def save_to_db(filename, Class):
    items = load_from_json(filename)
    for item in items:
        if Class == Product:
            for category in ProductCategory.objects.all():
                if item['category'] == category.name:
                    item['category'] = category
                    print(type(item['category']))
        obj = Class(**item)
        obj.save()
    print(f'Данные {filename} сохранены в базу данных')


save_to_db('categories.json', ProductCategory)
save_to_db('products.json', Product)