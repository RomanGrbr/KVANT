## Тестовое задание
- Создать проект в django, завести в базе данных таблицу со следующими полями:

Приоритет, число от 0 до 100, обязательное поле
Статус, строка не более 20 символов, обязательное поле, по умолчанию «created»
Время создания
Список исполнителей
Возможные значения статусов: создан, запущен, остановлен

- Прописать методы create, destroy

- Написать метод choose, выбирающий наиболее приоритетный объект со статусами «создан» и «остановлен», созданный раньше остальных.

- Написать скрипт на python, вызывающий метод choose, скрипт возвращает (и выводит на экран) id объекта

### Решение
- Клонировать репозиторий 'git clone ...'
- Установить зависимости 'pip install requirements.txt'
- Создать миграции 'python mange.py migrate'
- Создать суперюзера 'python mange.py createsuperuser'
- Добавить задачу 'python manage.py create [priority] [status] [list_of_performers]'
- Для получения самой приоритетной и старой задачи - запустить команду 'python manage.py choose'
- Удалить задачу 'python manage.py destroy [task_id]'
