from django.apps import AppConfig
from django.db.models.signals import post_migrate

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        # Import inside the ready() method to avoid AppRegistryNotReady
        from django.contrib.auth.models import Group, Permission

        def create_groups(sender, **kwargs):
            perms = Permission.objects.filter(content_type__app_label='bookshelf')

            editors, _ = Group.objects.get_or_create(name='Editors')
            editors.permissions.set(perms.filter(codename__in=['can_edit', 'can_create']))

            viewers, _ = Group.objects.get_or_create(name='Viewers')
            viewers.permissions.set(perms.filter(codename__in=['can_view']))

            admins, _ = Group.objects.get_or_create(name='Admins')
            admins.permissions.set(perms)

        post_migrate.connect(create_groups, sender=self)
