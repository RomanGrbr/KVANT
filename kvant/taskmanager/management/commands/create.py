from django.core.management.base import BaseCommand
from taskmanager.models import Task


class Command(BaseCommand):
    help = '''Команда создает задачу'''

    def add_arguments(self, parser):
        parser.add_argument('priority', nargs='+', type=int)
        parser.add_argument('status', nargs='+', type=str)
        parser.add_argument('list_of_performers', nargs='+')

    def handle(self, *args, **options):
        task_priority = options['priority'][0]
        task_status = options['status']
        task_list_of_performers = options['list_of_performers'][0]

        task = Task.objects.create(
            priority=task_priority,
            status=task_status,
            list_of_performers=task_list_of_performers
            )
        task.save()
        return f'Задача с id={task.id} создана'
