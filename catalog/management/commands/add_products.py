from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add products to the DB'

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name_category='Безопасность', description='Защита от вирусов, взлома и тд.')

        products = [
            {
                'name_product': 'Касперский Premium',
                'description': 'Лучший антивирус на рынке на год',
                'category': category,
                'price': 22
            },
            {
                'name_product': 'Касперский Plus',
                'description': 'Лучший антивирус на рынке на год',
                'category': category,
                'price': 21
            },
            {
                'name_product': 'Касперский Standard',
                'description': 'Лучший антивирус на рынке на год',
                'category': category,
                'price': 17
            }
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name_product}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name_product}'))
