import os
import json

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    # 1 вариант:
    # def handle(self, *args, **options):
    #     Category.objects.all().delete()
    #     Product.objects.all().delete()
    #     return os.system("python manage.py loaddata catalog.json")

    # 2 вариант:

    def handle(self, *args, **options):
        with open('./catalog.json', 'r', encoding='utf-8') as f:
            the_list = json.loads(f.read())

        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_to_fill = []
        products_to_fill = []
        index_for_products = {}
        for item in the_list:
            if item['model'] == 'catalog.category':
                temp = Category(**item['fields'])
                categories_to_fill.append(temp)
                index_for_products |= ({item['pk']: temp})
            elif item['model'] == 'catalog.product':
                products_to_fill.append(Product(name=item['fields']['name'],
                                                description=item['fields']['description'],
                                                image=item['fields']['image'],
                                                category=index_for_products[item['fields']['category']],
                                                price=item['fields']['price'],
                                                data_created=item['fields']['data_created'],
                                                data_updated=item['fields']['data_updated']))
        Category.objects.bulk_create(categories_to_fill)
        Product.objects.bulk_create(products_to_fill)
