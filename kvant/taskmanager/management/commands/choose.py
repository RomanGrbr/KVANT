from django.core.management.base import BaseCommand
from taskmanager.models import Task


class Command(BaseCommand):
    help = '''Команда возвращает id самой приоритетной и при этом самой
    старойзадачи, которая еще не была запущена.'''

    def handle(self, *args, **options):
        queryset = Task.objects.exclude(status='run')
        if len(queryset):
            return str(queryset[0].id)
        return 'Нет приритетных задач'
