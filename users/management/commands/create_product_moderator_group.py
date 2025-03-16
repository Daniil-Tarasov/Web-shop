from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        group_name = 'Product Moderator'
        permissions = [
            'catalog.can_unpublish_product',
            'catalog.can_delete_product'
        ]

        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            self.stdout.write(self.style.SUCCES(f'Группа "{group_name}" создана.'))
        else:
            self.stdout.write(self.style.WARNING(f'Группа "{group_name}" уже существует.'))

        for perm_name in permissions:
            perm = Permission.objects.get(codename=perm_name)
            group.permissions.add(perm)

        group.save()
