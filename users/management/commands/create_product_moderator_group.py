from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        group_name = 'Product Moderator'
        unpublish_permissions = Permission.objects.get(codename='can_unpublish_product')
        delete_permissions = Permission.objects.get(codename='delete_product')

        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" создана.'))
        else:
            self.stdout.write(self.style.WARNING(f'Группа "{group_name}" уже существует.'))

        group.permissions.add(unpublish_permissions, delete_permissions)

        group.save()
