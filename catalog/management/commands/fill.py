from django.core.management import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
                {'category_name': 'Бакалея', 'description': 'хлеб, лепешки'},
                {'category_name': 'Фрукты', 'description': 'свежие фрукты'},
                {'category_name': 'Овощи', 'description': 'свежие овощи'}
                ] 
        
        category_for_create = []
        categories = {}

        for category in category_list:
            category_for_create.append(Category(**category))
            
        Category.objects.bulk_create(category_for_create)

        for category in category_list:
            categories[category.get('category_name')] = Category.objects.filter(category_name=category.get('category_name'))[0]

        products_list = [
                {'product_name': 'Хлеб', 'product_description': 'свежий, только из печки', 'price': 50.00, 'category': categories.get('Бакалея')},
                {'product_name': 'Лепешка', 'product_description': 'испекли утром', 'price': 40.00, 'category': categories.get('Бакалея')},
                {'product_name': 'Яблоки', 'product_description': 'вкусные', 'price': 180.00, 'category': categories.get('Фрукты')},
                {'product_name': 'Арбуз', 'product_description': 'то что надо летним вечером', 'price': 230.00, 'category': categories.get('Фрукты')},
                {'product_name': 'Картофель', 'product_description': 'Обычная картошка', 'price': 125.00, 'category': categories.get('Овощи')},
                {'product_name': 'Морковь', 'product_description': 'Сидит девица в темнице а коса на улице', 'price': 140.00, 'category': categories.get('Овощи')},
                {'product_name': 'Лук', 'product_description': 'Аж расплакался пока его нарезал', 'price': 90.00, 'category': categories.get('Овощи')},
                ]

        products_for_create = []


        for product in products_list:
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)


