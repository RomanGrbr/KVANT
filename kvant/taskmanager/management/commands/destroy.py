from django.core.management.base import BaseCommand
from taskmanager.models import Task


class Command(BaseCommand):
    help = '''Команда удаляет задачу по переданному id'''

    def add_arguments(self, parser):
        parser.add_argument('task_id', nargs='+', type=int)

    def handle(self, *args, **options):
        taskid = options['task_id'][0]
        task = Task.objects.filter(id=taskid)
        task.delete()
        return f'Задача с id={taskid} удалена'
